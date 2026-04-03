/// Minimal Mach-O 64-bit Writer
///
/// Produces a minimal Mach-O executable for macOS with:
/// - Mach-O header
/// - LC_SEGMENT_64 containing __TEXT,__text
/// - LC_MAIN specifying the entry point offset

/// Mach-O magic number for 64-bit
const MH_MAGIC_64: u32 = 0xfeedfacf;
/// CPU type: x86_64
const CPU_TYPE_X86_64: u32 = 0x01000007;
/// CPU subtype: all
const CPU_SUBTYPE_ALL: u32 = 3;
/// File type: MH_EXECUTE
const MH_EXECUTE: u32 = 2;
/// Load command: LC_SEGMENT_64
const LC_SEGMENT_64: u32 = 0x19;
/// Load command: LC_MAIN
const LC_MAIN: u32 = 0x80000028;

/// Write a minimal Mach-O 64-bit executable
pub fn write_macho(code: &[u8], text_vaddr: u64) -> Vec<u8> {
    let mut macho = Vec::new();

    // Layout calculation
    let header_size: u32 = 32;       // Mach-O header
    let seg_cmd_size: u32 = 72 + 80; // LC_SEGMENT_64 + 1 section
    let main_cmd_size: u32 = 24;     // LC_MAIN
    let total_cmds_size = seg_cmd_size + main_cmd_size;
    let text_offset = header_size + total_cmds_size;
    let file_size = text_offset as usize + code.len();

    // ── Mach-O Header (32 bytes) ──
    macho.extend_from_slice(&MH_MAGIC_64.to_le_bytes());
    macho.extend_from_slice(&CPU_TYPE_X86_64.to_le_bytes());
    macho.extend_from_slice(&CPU_SUBTYPE_ALL.to_le_bytes());
    macho.extend_from_slice(&MH_EXECUTE.to_le_bytes());
    macho.extend_from_slice(&2u32.to_le_bytes());           // ncmds = 2
    macho.extend_from_slice(&total_cmds_size.to_le_bytes()); // sizeofcmds
    macho.extend_from_slice(&0u32.to_le_bytes());            // flags
    macho.extend_from_slice(&0u32.to_le_bytes());            // reserved (64-bit)

    // ── LC_SEGMENT_64: __TEXT ──
    macho.extend_from_slice(&LC_SEGMENT_64.to_le_bytes());
    macho.extend_from_slice(&seg_cmd_size.to_le_bytes());    // cmdsize
    // segname: "__TEXT\0\0\0\0\0\0\0\0\0\0\0" (16 bytes)
    let mut segname = [0u8; 16];
    segname[..6].copy_from_slice(b"__TEXT");
    macho.extend_from_slice(&segname);
    macho.extend_from_slice(&text_vaddr.to_le_bytes());      // vmaddr
    macho.extend_from_slice(&(file_size as u64).to_le_bytes()); // vmsize
    macho.extend_from_slice(&0u64.to_le_bytes());            // fileoff
    macho.extend_from_slice(&(file_size as u64).to_le_bytes()); // filesize
    macho.extend_from_slice(&5u32.to_le_bytes());            // maxprot: VM_PROT_READ|EXECUTE
    macho.extend_from_slice(&5u32.to_le_bytes());            // initprot
    macho.extend_from_slice(&1u32.to_le_bytes());            // nsects = 1
    macho.extend_from_slice(&0u32.to_le_bytes());            // flags

    // Section: __text within __TEXT (80 bytes)
    let mut sectname = [0u8; 16];
    sectname[..6].copy_from_slice(b"__text");
    macho.extend_from_slice(&sectname);                       // sectname
    macho.extend_from_slice(&segname);                        // segname
    macho.extend_from_slice(&(text_vaddr + text_offset as u64).to_le_bytes()); // addr
    macho.extend_from_slice(&(code.len() as u64).to_le_bytes()); // size
    macho.extend_from_slice(&text_offset.to_le_bytes());      // offset
    macho.extend_from_slice(&0u32.to_le_bytes());             // align (2^0 = 1)
    macho.extend_from_slice(&0u32.to_le_bytes());             // reloff
    macho.extend_from_slice(&0u32.to_le_bytes());             // nreloc
    // flags: S_ATTR_PURE_INSTRUCTIONS | S_ATTR_SOME_INSTRUCTIONS
    macho.extend_from_slice(&0x80000400u32.to_le_bytes());
    macho.extend_from_slice(&0u32.to_le_bytes());             // reserved1
    macho.extend_from_slice(&0u32.to_le_bytes());             // reserved2
    macho.extend_from_slice(&0u32.to_le_bytes());             // reserved3 (64-bit)

    // ── LC_MAIN ──
    macho.extend_from_slice(&LC_MAIN.to_le_bytes());
    macho.extend_from_slice(&main_cmd_size.to_le_bytes());
    macho.extend_from_slice(&(text_offset as u64).to_le_bytes()); // entryoff
    macho.extend_from_slice(&0u64.to_le_bytes());                 // stacksize (0 = default)

    // ── .text section (machine code) ──
    assert_eq!(macho.len(), text_offset as usize);
    macho.extend_from_slice(code);

    macho
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_macho_magic() {
        let code = vec![0xc3]; // ret
        let macho = write_macho(&code, 0x100000000);
        let magic = u32::from_le_bytes(macho[0..4].try_into().unwrap());
        assert_eq!(magic, MH_MAGIC_64);
    }

    #[test]
    fn test_macho_cpu_type() {
        let code = vec![0xc3];
        let macho = write_macho(&code, 0x100000000);
        let cpu = u32::from_le_bytes(macho[4..8].try_into().unwrap());
        assert_eq!(cpu, CPU_TYPE_X86_64);
    }
}

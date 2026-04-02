fn main() {
    println!("NEXUS-6 v0.1.0");
    println!(
        "Metal GPU: {}",
        if nexus6::gpu::is_available() {
            "available"
        } else {
            "not available (using CPU fallback)"
        }
    );
}

use rayon::prelude::*;
use tch::{Device, Tensor};

/// Stress test on the CPU
pub fn stress_cpu() {
    println!("Running CPU stress test...");
    let x = Tensor::randn(&[10_000, 10_000], (tch::Kind::Float, Device::Cpu));
    let _y = &x * &x;
    println!("CPU stress test completed.");
}

/// Stress test on a single GPU
pub fn stress_gpu() {
    println!("Running GPU stress test...");
    let device = Device::Cuda(0);
    let x = Tensor::randn(&[10_000, 10_000], (tch::Kind::Float, device));
    let _y = &x * &x;
    println!("GPU stress test completed.");
}

/// Stress test on a GPU with multiple threads feeding it
pub fn stress_tgpu() {
    println!("Running multi-threaded GPU stress test...");
    let device = Device::Cuda(0);

    (0..8).into_par_iter().for_each(|_| {
        let x = Tensor::randn(&[5_000, 5_000], (tch::Kind::Float, device));
        let _y = &x * &x;
    });

    println!("Threaded GPU stress test completed.");
}

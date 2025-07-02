#!/usr/bin/env python3

from rmqrcode import rMQR, ErrorCorrectionLevel, FitStrategy
from rmqrcode import QRImage

def main():
    print("rMQR Code Generator (Interactive CLI)\n")

    # Step 1: Data input
    data = input("Enter the text to encode: ").strip()
    if not data:
        print("No data provided. Exiting.")
        return

    # Step 2: Output file name
    output = input("Enter output file name (e.g., output.png): ").strip()
    if not output.endswith(".png"):
        output += ".png"

    # Step 3: Error Correction Level
    ecc_input = input("Choose error correction level ([M]/H): ").strip().upper()
    ecc = ErrorCorrectionLevel.H if ecc_input == 'H' else ErrorCorrectionLevel.M

    # Step 4: Fit Strategy
    print("\nChoose fit strategy:")
    print("  1. Minimize Width")
    print("  2. Minimize Height")
    print("  3. Balanced (default)")
    fit_choice = input("Enter choice (1/2/3): ").strip()

    fit_map = {
        '1': FitStrategy.MINIMIZE_WIDTH,
        '2': FitStrategy.MINIMIZE_HEIGHT,
        '3': FitStrategy.BALANCED
    }
    strategy = fit_map.get(fit_choice, FitStrategy.BALANCED)

    # Step 5: Module size with options
    print("\nChoose module size (pixel size per block):")
    print("  1. 4px")
    print("  2. 6px")
    print("  3. 8px (default)")
    print("  4. 10px")
    print("  5. 12px")
    size_choice = input("Enter choice (1-5): ").strip()

    module_size_map = {
        '1': 4,
        '2': 6,
        '3': 8,
        '4': 10,
        '5': 12
    }
    module_size = module_size_map.get(size_choice, 8)

    # Generate rMQR
    print("\nGenerating rMQR...")
    qr = rMQR.fit(data, ecc=ecc, fit_strategy=strategy)

    # Save to PNG
    img = QRImage(qr, module_size=module_size)
    img.save(output)

    print(f"\nrMQR code saved to '{output}'\n")

if __name__ == '__main__':
    main()

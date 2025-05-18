import argparse
from deformer import wave_deform, heat_deform

def main():
    parser = argparse.ArgumentParser(description="Image deformation tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # wave
    wave_parser = subparsers.add_parser("wave", help="deform the image using a wave equation")
    wave_parser.add_argument("--input1", required=True)
    wave_parser.add_argument("--input2", required=True)
    wave_parser.add_argument("--output", default="wave_result.gif")
    wave_parser.add_argument("--num-iter", type=int, default=240)
    wave_parser.add_argument("--skip-step", type=int, default=1)
    wave_parser.add_argument("--weight", type=float, default=0.2)
    wave_parser.add_argument("--noise-freq", type=int, default=None)
    wave_parser.add_argument("--noise-strength", type=float, default=0.0)

    # heat
    heat_parser = subparsers.add_parser("heat", help="blur the image with the heat equation")
    heat_parser.add_argument("--input", required=True)
    heat_parser.add_argument("--output", default="heat_result.gif")
    heat_parser.add_argument("--num-iter", type=int, default=240)
    heat_parser.add_argument("--skip-step", type=int, default=1)
    heat_parser.add_argument("--weight", type=float, default=0.2)
    heat_parser.add_argument("--noise-freq", type=int, default=None)
    heat_parser.add_argument("--noise-strength", type=float, default=0.0)

    args = parser.parse_args()

    if args.command == "wave":
        wave_deform(
            img1_path=args.input1,
            img2_path=args.input2,
            output_path=args.output,
            num_iter=args.num_iter,
            skip_step=args.skip_step,
            weight=args.weight,
            noise_freq=args.noise_freq,
            noise_strength=args.noise_strength,
        )
    elif args.command == "heat":
        heat_deform(
            img_path=args.input,
            output_path=args.output,
            num_iter=args.num_iter,
            skip_step=args.skip_step,
            weight=args.weight,
            noise_freq=args.noise_freq,
            noise_strength=args.noise_strength,    
        )

if __name__ == "__main__":
    main()
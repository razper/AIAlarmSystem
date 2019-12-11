import argparse


class Parser:
    parser = argparse.ArgumentParser(description='Smart Artificial Intelligence System')
    parser.add_argument('--token', required=True, help='Token key')
    parser.add_argument('--camera_type', type=int, required=False, choices=[0, 1],
                        default=1, help='camera type 0 for primary camera, 1 for external')
    parser.add_argument('--proxy', help='using specific proxy, WITHOUT http:// or https://', default=None)
    args = parser.parse_args()
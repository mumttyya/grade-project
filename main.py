#!/usr/bin/env python3

from lib.cli import GradeMasterCLI

def main():
    """Main entry point for the GradeMaster CLI application"""
    try:
        app = GradeMasterCLI()
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for using GradeMaster!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
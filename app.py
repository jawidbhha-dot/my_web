import os
import sys
import webview

def run_app():
    # Path to index.html
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(base_dir, "index.html")

    if not os.path.exists(html_file):
        print(f"Error: Could not find {html_file}")
        sys.exit(1)

    # Create standalone desktop window
    window = webview.create_window(
        title="OptiScan AI — Medical Eye Screening App",
        url=f"file:///{html_file.replace(os.sep, '/')}",
        width=1000,
        height=820,
        min_size=(640, 600),
        resizable=True,
        text_select=True,
        background_color="#F8FAFC"
    )

    webview.start()

if __name__ == "__main__":
    run_app()

import ffmpeg

if __name__ == "__main__":
    out, _ = (
        ffmpeg
        .input('test.mov')
        .output('test.webm', vcodec='libvpx-vp9', pix_fmt='yuva420p', bitrate='2M')
        .run(capture_stdout=True)
    )
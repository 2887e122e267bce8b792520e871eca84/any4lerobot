import ffmpeg

# Convert AV1 to H.264
ffmpeg.input('sample_lerobot_data/videos/observation.images.cam_high/chunk-000/file-000.mp4').output('video_h264.mp4', vcodec='libx264').run()
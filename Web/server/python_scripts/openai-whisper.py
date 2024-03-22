# # # python3 cli.py ../test3/test2.mp4 -ms 1000
# # import os
# # from datetime import datetime
# # import ffmpeg
# # import whisper
# # import argparse
# # import warnings
# # import tempfile
# # import utils.translate_srt as translate_srt
# # import utils.overlay_audio_on_video as overlay_audio_on_video
# # import utils.gender_labeling as gender_labeling
# # import utils.SRTToWAV as SRTToWAV
# # import utils.createVideoOutput as createVideoOutput
# # from utils.srtToTxt import srt_to_txt_v2
# # from utils.utils import filename, str2bool, write_srt, mp4_to_wav, noise_deepfilternet, read_video_info, srt_to_txt
# # import pytube
# # import uuid
# # import re
# # import json
# # from time import gmtime, strftime
# # import logging

# # # Thiết lập cấu hình logging
# # logging.basicConfig(filename='logfile.log', level=logging.ERROR, format='%(asctime)s - %(message)s')
# # def main():
# #     parser = argparse.ArgumentParser(
# #         formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# #     parser.add_argument("video", nargs="+", type=str,
# #                         help="paths to video files to transcribe")
# #     parser.add_argument('-r', '--rate', type=int, default=10, 
# #                         help='Rate for speech (default: 0)')
# #     parser.add_argument('-v', '--volume', type=int, default=50, 
# #                         help='Volume for speech (default: 50)')
# #     parser.add_argument("-ms", "--ms_start", type=int, default=0, 
# #                         help="Start time in milliseconds for overlaying the audio on the video.")
# #     parser.add_argument("-noise", "--algorithm_noise", type=str2bool, default=False,
# #                         help="Chọn thuật toán giảm nhiễu")
# #     parser.add_argument("--model", default="small",
# #                         choices=whisper.available_models(), help="name of the Whisper model to use")
# #     parser.add_argument("--output_dir", "-o", type=str,
# #                         default=".", help="directory to save the outputs")
# #     parser.add_argument("--output_srt", type=str2bool, default=False,
# #                         help="whether to output the .srt file along with the video files")
# #     parser.add_argument("--srt_only", type=str2bool, default=True,
# #                         help="only generate the .srt file and not create overlayed video")
# #     parser.add_argument("--subtitle_vi", type=str2bool, default=True,
# #                         help="create videos with Vietnamese subtitles?")
# #     parser.add_argument("--ad_subtitle_en", type=str2bool, default=False,
# #                         help="Create a voice-over video with English subtitles?")
# #     parser.add_argument("--retain_sound", type=str2bool, default=True, 
# #                         help="retain the original sound")
# #     parser.add_argument("--verbose", type=str2bool, default=False,
# #                         help="whether to print out the progress and debug messages")
# #     parser.add_argument("--gender", type=str, default="auto", choices=[
# #                         "auto", "female", "male"], help="Gender recognition for Text To Speech model")
# #     parser.add_argument("--task", type=str, default="transcribe", choices=[
# #                         "transcribe", "translate"], help="whether to perform X->X speech recognition ('transcribe') or X->English translation ('translate')")
# #     parser.add_argument("--l_in", type=str, default="auto", choices=["auto","af","am","ar","as","az","ba","be","bg","bn","bo","br","bs","ca","cs","cy","da","de","el","en","es","et","eu","fa","fi","fo","fr","gl","gu","ha","haw","he","hi","hr","ht","hu","hy","id","is","it","ja","jw","ka","kk","km","kn","ko","la","lb","ln","lo","lt","lv","mg","mi","mk","ml","mn","mr","ms","mt","my","ne","nl","nn","no","oc","pa","pl","ps","pt","ro","ru","sa","sd","si","sk","sl","sn","so","sq","sr","su","sv","sw","ta","te","tg","th","tk","tl","tr","tt","uk","ur","uz","vi","yi","yo","zh"], 
# #     help="What is the origin language of the video? If unset, it is detected automatically.")

# #     time_text = str(strftime("%Y%m%d_%H%M%S", gmtime())) 
# #     start_time = datetime.now()
# #     args = parser.parse_args().__dict__
# #     path = args.pop("video")
# #     input_arg = path[0]
# #     # root_path = os.path.dirname(input_arg) + '/'
# #     model_name: str = args.pop("model")
# #     output_dir: str = args.pop("output_dir")
# #     # output_dir = root_path
# #     output_srt: bool = args.pop("output_srt")
# #     srt_only: bool = args.pop("srt_only")
# #     subtitle_vi: bool = args.pop("subtitle_vi")
# #     ad_subtitle_en: bool = args.pop("ad_subtitle_en")
# #     algorithm_noise: bool = args.pop("algorithm_noise")
# #     retain_sound: bool = args.pop("retain_sound")
# #     language: str = args.pop("l_in")
# #     gender: str = args.pop("gender")
# #     rate : int = args.pop("rate")
# #     volume : int = args.pop("volume")
# #     ms_start : int = args.pop("ms_start")
# #     os.makedirs(output_dir, exist_ok=True)

# #     logging.error('Command: python3 openai-whisper.py %s --l_in %s -r %d -v %d --ad_subtitle_en %r --retain_sound %r -noise %r --gender %s', 
# #                     path, language, rate, volume, ad_subtitle_en, retain_sound, algorithm_noise, gender)
# #     if input_arg.startswith('https://www.youtube.com'):
# #         video_path = download_youtube_video(input_arg, '../public/videos')
# #         print("Video youtube đã được lưu vào: "+ video_path)
# #         path[0] = video_path
# #         input_arg = video_path
# #     root_path = os.path.dirname(input_arg) + '/'
# #     output_dir = root_path

# #     if model_name.endswith(".en"):
# #         warnings.warn(
# #             f"{model_name} is an English-only model, forcing English detection.")
# #         args["language"] = "en"
# #     # if translate task used and language argument is set, then use it
# #     elif language != "auto":
# #         args["language"] = language
        

# #     path_wav = mp4_to_wav(input_arg)
# #     print("Path wav gốc:")
# #     print(path_wav)
# #     if algorithm_noise:
# #         path_wav_handled = noise_deepfilternet(path_wav)
# #         print("Path wav đã lọc nhiễu:")
# #         print(path_wav_handled)
# #     else:
# #         print("Không có giảm nhiễu")
# #         path_wav_handled = path_wav

# #     model = whisper.load_model(model_name)
# #     audios = {input_arg: path_wav_handled}
# #     print("----------------------------------------------------------------") # {'../public/videos/f8c1496e.mp4': '../public/videos/f8c1496e_DeepFilterNet3.wav'}
# #     print(audios)
# #     # audios = get_audio(path)
# #     # print("----------------------------------------------------------------") # {'../public/videos/d50aee64.mp4': '/tmp/d50aee64.wav'}
# #     # print(audios)
# #     srt_path = get_subtitles(
# #         audios, output_srt or srt_only, output_dir, lambda audio_path: model.transcribe(audio_path, **args)
# #     )
    
# #     if srt_only:
# #         print("path srt gốc: "+ srt_path)
# #         path_txt = srt_to_txt_v2(srt_path)
# #         print("path txt gốc: "+ path_txt)
# #         path_srt_translated = translate_srt.translate_and_save_srt(srt_path)
# #         print("path srt đã dịch sang tiếng việt: "+ path_srt_translated)
# #         # gender : auto
# #         if gender == 'auto':
# #             # gender classification and labels
# #             srt_labeled = gender_labeling.split_and_predict(path_srt_translated, path_wav_handled)
# #             print("path srt đã được gắn nhãn: "+ srt_labeled)
# #         if gender == 'female':
# #             srt_labeled = gender_labeling.label_srt_file(path_srt_translated, "(0)")
# #             print("path srt đã được gắn nhãn: "+ srt_labeled)
# #         if gender == 'male':
# #             srt_labeled = gender_labeling.label_srt_file(path_srt_translated, "(1)")
# #             print("path srt đã được gắn nhãn: "+ srt_labeled)

# #         # text to speech recognition
# #         captions = SRTToWAV.process_srt(srt_labeled)
# #         output_audio_path = SRTToWAV.text_to_speech(captions, srt_labeled, rate, volume)
# #         print(f"path wav thuyết minh: {output_audio_path}")
# #         audiodescribed_wav_path = overlay_audio_on_video.process_audio(path_wav, output_audio_path, ms_start, retain_sound)
# #         print("path wav thuyết minh được phủ với wav gốc:", audiodescribed_wav_path)
# #         audiodescribed_video_path = overlay_audio_on_video.merge_video_and_audio(input_arg, audiodescribed_wav_path)
# #         print("path video thuyết minh:", audiodescribed_video_path)
# #         ad_subtitle_video_path= None
# #         if ad_subtitle_en:
# #             ad_subtitle_video_path  = createVideoOutput.createAudiodescribed(audiodescribed_video_path, srt_path)
# #             print("path video thuyết minh có phụ đề:", ad_subtitle_video_path)
# #         if subtitle_vi:
# #             subtitle_video_path = createVideoOutput.createSubtitle(input_arg,path_srt_translated)
# #             print("path video phụ đề:", subtitle_video_path)
# #         capacity, time = read_video_info(input_arg)
# #         end_time = datetime.now()
# #         time_difference = end_time - start_time
# #         seconds = time_difference.total_seconds()
# #         print("Thời gian thực thi: "+str(seconds))
        
# #         result = {
# #                 "date_time":time_text,
# #                 "path_video": input_arg,
# #                 "capacity": capacity,
# #                 "time": time,
# #                 "sourceLanguage": language,
# #                 "audio_original": path_wav,
# #                 "srt_original": srt_path,
# #                 "audio_filtered": path_wav_handled,
# #                 "srt_translated":path_srt_translated,
# #                 "srt_labeled": srt_labeled,
# #                 "audio_described":output_audio_path,
# #                 "audio_overlay_described":audiodescribed_wav_path,
# #                 "videoSubtitle": subtitle_video_path,
# #                 "video_explanation":audiodescribed_video_path,
# #                 "video_explanation_sub":ad_subtitle_video_path,
# #                 "execution_time": str(seconds)
# #                 }
# #         # Lưu kết quả vào log
# #         logging.error('Result: %s', result)
# #         return result

# # def get_audio(paths):
# #     temp_dir = tempfile.gettempdir()

# #     audio_paths = {}

# #     for path in paths:
# #         print(f"Extracting audio from {filename(path)}...")
# #         output_path = os.path.join(temp_dir, f"{filename(path)}.wav")

# #         ffmpeg.input(path).output(
# #             output_path,
# #             acodec="pcm_s16le", ac=1, ar="16k"
# #         ).run(quiet=True, overwrite_output=True)

# #         audio_paths[path] = output_path

# #     return audio_paths


# # def get_subtitles(audio_paths: list, output_srt: bool, output_dir: str, transcribe: callable):
# #     subtitles_path = {}

# #     for path, audio_path in audio_paths.items():
# #         srt_path = output_dir if output_srt else tempfile.gettempdir()
# #         srt_path = os.path.join(srt_path, f"{filename(path)}.srt")
        
# #         print(
# #             f"Generating subtitles for {filename(path)}... This might take a while."
# #         )

# #         warnings.filterwarnings("ignore")
# #         result = transcribe(audio_path)
# #         warnings.filterwarnings("default")

# #         with open(srt_path, "w", encoding="utf-8") as srt:
# #             write_srt(result["segments"], file=srt)

# #         subtitles_path[path] = srt_path
# #     return srt_path


# # def download_youtube_video(url, path):
# #     yt = pytube.YouTube(url)

# #     # Trích xuất ID từ tiêu đề video
# #     video_id_match = re.search(r'([a-zA-Z0-9_-]+)\.mp4$', yt.title)
# #     if video_id_match:
# #         video_id = video_id_match.group(1)
# #     else:
# #         # Nếu không tìm thấy ID, sử dụng chuỗi ngẫu nhiên
# #         video_id = str(uuid.uuid4().hex)[:8]

# #     # Tạo tên file mới
# #     video_name = f"{video_id}.mp4"
    
# #     # Thêm đường dẫn đầy đủ
# #     video_path = os.path.join(path, video_name)
    
# #     stream = yt.streams.filter(file_extension='mp4').first()
# #     stream.download(output_path=path, filename=video_name)
    
# #     return video_path


# # if __name__ == '__main__':
# #     result = main()
# #     print("--------------------------------END--------------------------------")
# #     print(json.dumps(result, indent=4))



# # python3 cli.py ../test3/test2.mp4 -ms 1000
# import os
# from datetime import datetime
# import ffmpeg
# import whisper
# import argparse
# import warnings
# import tempfile
# import utils.translate_srt as translate_srt
# import utils.overlay_audio_on_video as overlay_audio_on_video
# import utils.gender_labeling as gender_labeling
# import utils.SRTToWAV as SRTToWAV
# import utils.createVideoOutput as createVideoOutput
# from utils.srtToTxt import srt_to_txt_v2
# from utils.utils import filename, str2bool, write_srt, mp4_to_wav, noise_deepfilternet, read_video_info, srt_to_txt
# import pytube
# import uuid
# import re
# import json
# from time import gmtime, strftime
# import logging

# # Thiết lập cấu hình logging
# logging.basicConfig(filename='logfile.log', level=logging.ERROR, format='%(asctime)s - %(message)s')
# def main():
#     parser = argparse.ArgumentParser(
#         formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#     parser.add_argument("video", nargs="+", type=str,
#                         help="paths to video files to transcribe")
#     parser.add_argument('-r', '--rate', type=int, default=10, 
#                         help='Rate for speech (default: 0)')
#     parser.add_argument('-v', '--volume', type=int, default=50, 
#                         help='Volume for speech (default: 50)')
#     parser.add_argument("-ms", "--ms_start", type=int, default=0, 
#                         help="Start time in milliseconds for overlaying the audio on the video.")
#     parser.add_argument("-noise", "--algorithm_noise", type=str2bool, default=False,
#                         help="Chọn thuật toán giảm nhiễu")
#     parser.add_argument("--model", default="small",
#                         choices=whisper.available_models(), help="name of the Whisper model to use")
#     parser.add_argument("--output_dir", "-o", type=str,
#                         default=".", help="directory to save the outputs")
#     parser.add_argument("--output_srt", type=str2bool, default=False,
#                         help="whether to output the .srt file along with the video files")
#     parser.add_argument("--srt_only", type=str2bool, default=True,
#                         help="only generate the .srt file and not create overlayed video")
#     parser.add_argument("--subtitle_vi", type=str2bool, default=True,
#                         help="create videos with Vietnamese subtitles?")
#     parser.add_argument("--ad_subtitle_en", type=str2bool, default=False,
#                         help="Create a voice-over video with English subtitles?")
#     parser.add_argument("--retain_sound", type=str2bool, default=True, 
#                         help="retain the original sound")
#     parser.add_argument("--verbose", type=str2bool, default=False,
#                         help="whether to print out the progress and debug messages")
#     parser.add_argument("--gender", type=str, default="auto", choices=[
#                         "auto", "female", "male"], help="Gender recognition for Text To Speech model")
#     parser.add_argument("--task", type=str, default="transcribe", choices=[
#                         "transcribe", "translate"], help="whether to perform X->X speech recognition ('transcribe') or X->English translation ('translate')")
#     parser.add_argument("--l_in", type=str, default="auto", choices=["auto","af","am","ar","as","az","ba","be","bg","bn","bo","br","bs","ca","cs","cy","da","de","el","en","es","et","eu","fa","fi","fo","fr","gl","gu","ha","haw","he","hi","hr","ht","hu","hy","id","is","it","ja","jw","ka","kk","km","kn","ko","la","lb","ln","lo","lt","lv","mg","mi","mk","ml","mn","mr","ms","mt","my","ne","nl","nn","no","oc","pa","pl","ps","pt","ro","ru","sa","sd","si","sk","sl","sn","so","sq","sr","su","sv","sw","ta","te","tg","th","tk","tl","tr","tt","uk","ur","uz","vi","yi","yo","zh"], 
#     help="What is the origin language of the video? If unset, it is detected automatically.")

#     time_text = str(strftime("%Y%m%d_%H%M%S", gmtime())) 
#     start_time = datetime.now()
#     args = parser.parse_args().__dict__
#     path = args.pop("video")
#     input_arg = path[0]
#     # root_path = os.path.dirname(input_arg) + '/'
#     model_name: str = args.pop("model")
#     output_dir: str = args.pop("output_dir")
#     # output_dir = root_path
#     output_srt: bool = args.pop("output_srt")
#     srt_only: bool = args.pop("srt_only")
#     subtitle_vi: bool = args.pop("subtitle_vi")
#     ad_subtitle_en: bool = args.pop("ad_subtitle_en")
#     algorithm_noise: bool = args.pop("algorithm_noise")
#     retain_sound: bool = args.pop("retain_sound")
#     language: str = args.pop("l_in")
#     gender: str = args.pop("gender")
#     rate : int = args.pop("rate")
#     volume : int = args.pop("volume")
#     ms_start : int = args.pop("ms_start")
#     os.makedirs(output_dir, exist_ok=True)

#     logging.error('Command: python3 openai-whisper.py %s --l_in %s -r %d -v %d --ad_subtitle_en %r --retain_sound %r -noise %r --gender %s', 
#                     path, language, rate, volume, ad_subtitle_en, retain_sound, algorithm_noise, gender)
#     if input_arg.startswith('https://www.youtube.com'):
#         video_path = download_youtube_video(input_arg, '../public/videos')
#         print("Video youtube đã được lưu vào: "+ video_path)
#         path[0] = video_path
#         input_arg = video_path
#     root_path = os.path.dirname(input_arg) + '/'
#     output_dir = root_path

#     if model_name.endswith(".en"):
#         warnings.warn(
#             f"{model_name} is an English-only model, forcing English detection.")
#         args["language"] = "en"
#     # if translate task used and language argument is set, then use it
#     elif language != "auto":
#         args["language"] = language
        

#     path_wav = mp4_to_wav(input_arg)
#     print("Path wav gốc:")
#     print(path_wav)
#     if algorithm_noise:
#         path_wav_handled = noise_deepfilternet(path_wav)
#         print("Path wav đã lọc nhiễu:")
#         print(path_wav_handled)
#     else:
#         print("Không có giảm nhiễu")
#         path_wav_handled = path_wav

#     model = whisper.load_model(model_name)
#     audios = {input_arg: path_wav_handled}
#     print("----------------------------------------------------------------") # {'../public/videos/f8c1496e.mp4': '../public/videos/f8c1496e_DeepFilterNet3.wav'}
#     print(audios)
#     # audios = get_audio(path)
#     # print("----------------------------------------------------------------") # {'../public/videos/d50aee64.mp4': '/tmp/d50aee64.wav'}
#     # print(audios)
#     srt_path = get_subtitles(
#         audios, output_srt or srt_only, output_dir, lambda audio_path: model.transcribe(audio_path, **args)
#     )
    
#     if srt_only:
#         print("path srt gốc: "+ srt_path)
#         path_txt = srt_to_txt_v2(srt_path)
#         print("path txt gốc: "+ path_txt)
#         path_srt_translated = translate_srt.translate_and_save_srt(srt_path)
#         print("path srt đã dịch sang tiếng việt: "+ path_srt_translated)
#         # gender : auto
#         if gender == 'auto':
#             # gender classification and labels
#             srt_labeled = gender_labeling.split_and_predict(path_srt_translated, path_wav_handled)
#             print("path srt đã được gắn nhãn: "+ srt_labeled)
#         if gender == 'female':
#             srt_labeled = gender_labeling.label_srt_file(path_srt_translated, "(0)")
#             print("path srt đã được gắn nhãn: "+ srt_labeled)
#         if gender == 'male':
#             srt_labeled = gender_labeling.label_srt_file(path_srt_translated, "(1)")
#             print("path srt đã được gắn nhãn: "+ srt_labeled)

#         # text to speech recognition
#         captions = SRTToWAV.process_srt(srt_labeled)
#         output_audio_path = SRTToWAV.text_to_speech(captions, srt_labeled, rate, volume)
#         print(f"path wav thuyết minh: {output_audio_path}")
#         audiodescribed_wav_path = overlay_audio_on_video.process_audio(path_wav, output_audio_path, ms_start, retain_sound)
#         print("path wav thuyết minh được phủ với wav gốc:", audiodescribed_wav_path)
#         audiodescribed_video_path = overlay_audio_on_video.merge_video_and_audio(input_arg, audiodescribed_wav_path)
#         print("path video thuyết minh:", audiodescribed_video_path)
#         ad_subtitle_video_path= None
#         if ad_subtitle_en:
#             ad_subtitle_video_path  = createVideoOutput.createAudiodescribed(audiodescribed_video_path, srt_path)
#             print("path video thuyết minh có phụ đề:", ad_subtitle_video_path)
#         if subtitle_vi:
#             subtitle_video_path = createVideoOutput.createSubtitle(input_arg,path_srt_translated)
#             print("path video phụ đề:", subtitle_video_path)
#         capacity, time = read_video_info(input_arg)
#         end_time = datetime.now()
#         time_difference = end_time - start_time
#         seconds = time_difference.total_seconds()
#         print("Thời gian thực thi: "+str(seconds))
        
#         result = ', '+ time_text + ', ' + input_arg+ ', ' + capacity + ', ' + time + ', ' + language + ', ' + path_wav + ', ' + srt_path + ', ' + path_wav_handled + ', ' + path_srt_translated + ', ' + srt_labeled + ', '+ output_audio_path + ', '+ audiodescribed_wav_path + ', '+ subtitle_video_path + ', ' + audiodescribed_video_path + ', '+ ad_subtitle_video_path + ', ' + str(seconds)
#         # result = {
#         #     "date_time": str(time_text),
#         #     "path_video": str(input_arg),
#         #     "capacity": str(capacity),
#         #     "time": str(time),
#         #     "sourceLanguage": str(language),
#         #     "audio_original": str(path_wav),
#         #     "srt_original": str(srt_path),
#         #     "audio_filtered": str(path_wav_handled),
#         #     "srt_translated": str(path_srt_translated),
#         #     "srt_labeled": str(srt_labeled),
#         #     "audio_described": str(output_audio_path),
#         #     "audio_overlay_described": str(audiodescribed_wav_path),
#         #     "videoSubtitle": str(subtitle_video_path),
#         #     "video_explanation": str(audiodescribed_video_path),
#         #     "video_explanation_sub": str(ad_subtitle_video_path),
#         #     "execution_time": str(seconds)
#         # }

#         logging.error('Result: %s', result)
#         return result

# def get_audio(paths):
#     temp_dir = tempfile.gettempdir()

#     audio_paths = {}

#     for path in paths:
#         print(f"Extracting audio from {filename(path)}...")
#         output_path = os.path.join(temp_dir, f"{filename(path)}.wav")

#         ffmpeg.input(path).output(
#             output_path,
#             acodec="pcm_s16le", ac=1, ar="16k"
#         ).run(quiet=True, overwrite_output=True)

#         audio_paths[path] = output_path

#     return audio_paths


# def get_subtitles(audio_paths: list, output_srt: bool, output_dir: str, transcribe: callable):
#     subtitles_path = {}

#     for path, audio_path in audio_paths.items():
#         srt_path = output_dir if output_srt else tempfile.gettempdir()
#         srt_path = os.path.join(srt_path, f"{filename(path)}.srt")
        
#         print(
#             f"Generating subtitles for {filename(path)}... This might take a while."
#         )

#         warnings.filterwarnings("ignore")
#         result = transcribe(audio_path)
#         warnings.filterwarnings("default")

#         with open(srt_path, "w", encoding="utf-8") as srt:
#             write_srt(result["segments"], file=srt)

#         subtitles_path[path] = srt_path
#     return srt_path


# def download_youtube_video(url, path):
#     yt = pytube.YouTube(url)

#     # Trích xuất ID từ tiêu đề video
#     video_id_match = re.search(r'([a-zA-Z0-9_-]+)\.mp4$', yt.title)
#     if video_id_match:
#         video_id = video_id_match.group(1)
#     else:
#         # Nếu không tìm thấy ID, sử dụng chuỗi ngẫu nhiên
#         video_id = str(uuid.uuid4().hex)[:8]

#     # Tạo tên file mới
#     video_name = f"{video_id}.mp4"
    
#     # Thêm đường dẫn đầy đủ
#     video_path = os.path.join(path, video_name)
    
#     stream = yt.streams.filter(file_extension='mp4').first()
#     stream.download(output_path=path, filename=video_name)
    
#     return video_path


# if __name__ == '__main__':
#     result = main()
#     print(result)




# python3 cli.py ../test3/test2.mp4 -ms 1000
import os
from datetime import datetime
import ffmpeg
import whisper
import argparse
import warnings
import tempfile
import utils.translate_srt as translate_srt
import utils.overlay_audio_on_video as overlay_audio_on_video
import utils.gender_labeling as gender_labeling
import utils.SRTToWAV as SRTToWAV
import utils.createVideoOutput as createVideoOutput
from utils.srtToTxt import srt_to_txt_v2
from utils.removeSpeech import removeSpeech
from utils.utils import filename, str2bool, write_srt, mp4_to_wav, noise_deepfilternet, read_video_info, srt_to_txt
import pytube
import uuid
import re
import json
from time import gmtime, strftime
import logging
import youtube_dl
# Thiết lập cấu hình logging
logging.basicConfig(filename='logfile.log', level=logging.ERROR, format='%(asctime)s - %(message)s')
def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("video", nargs="+", type=str,
                        help="paths to video files to transcribe")
    parser.add_argument('-r', '--rate', type=int, default=10, 
                        help='Rate for speech (default: 0)')
    parser.add_argument('-v', '--volume', type=int, default=50, 
                        help='Volume for speech (default: 50)')
    parser.add_argument("-ms", "--ms_start", type=int, default=0, 
                        help="Start time in milliseconds for overlaying the audio on the video.")
    parser.add_argument("-noise", "--algorithm_noise", type=str2bool, default=False,
                        help="Chọn thuật toán giảm nhiễu")
    parser.add_argument("--model", default="small",
                        choices=whisper.available_models(), help="name of the Whisper model to use")
    parser.add_argument("--output_dir", "-o", type=str,
                        default=".", help="directory to save the outputs")
    parser.add_argument("--output_srt", type=str2bool, default=False,
                        help="whether to output the .srt file along with the video files")
    parser.add_argument("--srt_only", type=str2bool, default=True,
                        help="only generate the .srt file and not create overlayed video")
    parser.add_argument("--subtitle_vi", type=str2bool, default=True,
                        help="create videos with Vietnamese subtitles?")
    parser.add_argument("--ad_subtitle_en", type=str2bool, default=False,
                        help="Create a voice-over video with English subtitles?")
    parser.add_argument("--retain_sound", type=str2bool, default=True, 
                        help="retain the original sound")
    parser.add_argument("--verbose", type=str2bool, default=False,
                        help="whether to print out the progress and debug messages")
    parser.add_argument("--gender", type=str, default="auto", choices=[
                        "auto", "female", "male"], help="Gender recognition for Text To Speech model")
    parser.add_argument("--task", type=str, default="transcribe", choices=[
                        "transcribe", "translate"], help="whether to perform X->X speech recognition ('transcribe') or X->English translation ('translate')")
    parser.add_argument("--l_in", type=str, default="auto", choices=["auto","af","am","ar","as","az","ba","be","bg","bn","bo","br","bs","ca","cs","cy","da","de","el","en","es","et","eu","fa","fi","fo","fr","gl","gu","ha","haw","he","hi","hr","ht","hu","hy","id","is","it","ja","jw","ka","kk","km","kn","ko","la","lb","ln","lo","lt","lv","mg","mi","mk","ml","mn","mr","ms","mt","my","ne","nl","nn","no","oc","pa","pl","ps","pt","ro","ru","sa","sd","si","sk","sl","sn","so","sq","sr","su","sv","sw","ta","te","tg","th","tk","tl","tr","tt","uk","ur","uz","vi","yi","yo","zh"], 
    help="What is the origin language of the video? If unset, it is detected automatically.")

    time_text = str(strftime("%Y%m%d_%H%M%S", gmtime())) 
    start_time = datetime.now()
    args = parser.parse_args().__dict__
    path = args.pop("video")
    input_arg = path[0]
    # root_path = os.path.dirname(input_arg) + '/'
    model_name: str = args.pop("model")
    output_dir: str = args.pop("output_dir")
    # output_dir = root_path
    output_srt: bool = args.pop("output_srt")
    srt_only: bool = args.pop("srt_only")
    subtitle_vi: bool = args.pop("subtitle_vi")
    ad_subtitle_en: bool = args.pop("ad_subtitle_en")
    algorithm_noise: bool = args.pop("algorithm_noise")
    retain_sound: bool = args.pop("retain_sound")
    language: str = args.pop("l_in")
    gender: str = args.pop("gender")
    rate : int = args.pop("rate")
    volume : int = args.pop("volume")
    ms_start : int = args.pop("ms_start")
    os.makedirs(output_dir, exist_ok=True)

    logging.error('Command: python3 openai-whisper.py %s --l_in %s -r %d -v %d --ad_subtitle_en %r --retain_sound %r -noise %r --gender %s', 
                    path, language, rate, volume, ad_subtitle_en, retain_sound, algorithm_noise, gender)
    if input_arg.startswith('https://www.youtube.com'):
        video_path = download_youtube_video(input_arg, '../public/videos')
        path[0] = video_path
        input_arg = video_path
    root_path = os.path.dirname(input_arg) + '/'
    output_dir = root_path

    if model_name.endswith(".en"):
        warnings.warn(
            f"{model_name} is an English-only model, forcing English detection.")
        args["language"] = "en"
    # if translate task used and language argument is set, then use it
    elif language != "auto":
        args["language"] = language
        

    path_wav = mp4_to_wav(input_arg)
    if algorithm_noise:
        path_wav_handled = noise_deepfilternet(path_wav)
    else:
        path_wav_handled = path_wav

    model = whisper.load_model(model_name)
    audios = {input_arg: path_wav_handled}
    srt_path = get_subtitles(
        audios, output_srt or srt_only, output_dir, lambda audio_path: model.transcribe(audio_path, **args)
    )
    
    if srt_only:
        path_txt = srt_to_txt_v2(srt_path)
        path_srt_translated = translate_srt.translate_and_save_srt(srt_path)
        # gender : auto
        if gender == 'auto':
            # gender classification and labels
            srt_labeled = gender_labeling.split_and_predict(path_srt_translated, path_wav_handled)
        if gender == 'female':
            srt_labeled = gender_labeling.label_srt_file(path_srt_translated, "(0)")
        if gender == 'male':
            srt_labeled = gender_labeling.label_srt_file(path_srt_translated, "(1)")

        # text to speech recognition
        captions = SRTToWAV.process_srt(srt_labeled)
        output_audio_path = SRTToWAV.text_to_speech(captions, srt_labeled, rate, volume)
        if retain_sound:
            audiodescribed_wav_path = overlay_audio_on_video.process_audio(path_wav, path_wav, output_audio_path, ms_start, retain_sound)
        else:
            audio_removed_speech = removeSpeech(path_wav)
            audiodescribed_wav_path = overlay_audio_on_video.process_audio(path_wav, audio_removed_speech, output_audio_path, ms_start, retain_sound)
            
        audiodescribed_video_path = overlay_audio_on_video.merge_video_and_audio(input_arg, audiodescribed_wav_path)
        ad_subtitle_video_path= None
        if ad_subtitle_en:
            ad_subtitle_video_path  = createVideoOutput.createAudiodescribed(audiodescribed_video_path, srt_path)
        if subtitle_vi:
            subtitle_video_path = createVideoOutput.createSubtitle(input_arg,path_srt_translated)
        capacity, time = read_video_info(input_arg)
        end_time = datetime.now()
        time_difference = end_time - start_time
        seconds = time_difference.total_seconds()
        result = {"date_time":time_text,
                "path_video": input_arg,
                "capacity": capacity,
                "time": time,
                "sourceLanguage": language,
                "audio_original": path_wav,
                "srt_original": srt_path,
                "audio_filtered": path_wav_handled,
                "srt_translated":path_srt_translated,
                "srt_labeled": srt_labeled,
                "audio_described":output_audio_path,
                "audio_overlay_described":audiodescribed_wav_path,
                "videoSubtitle": subtitle_video_path,
                "video_explanation":audiodescribed_video_path,
                "video_explanation_sub":ad_subtitle_video_path,
                "execution_time": str(seconds)
                }
        # Lưu kết quả vào log
        logging.error('Result: %s', result)
        return result

def get_audio(paths):
    temp_dir = tempfile.gettempdir()

    audio_paths = {}

    for path in paths:
        output_path = os.path.join(temp_dir, f"{filename(path)}.wav")

        ffmpeg.input(path).output(
            output_path,
            acodec="pcm_s16le", ac=1, ar="16k"
        ).run(quiet=True, overwrite_output=True)

        audio_paths[path] = output_path

    return audio_paths


def get_subtitles(audio_paths: list, output_srt: bool, output_dir: str, transcribe: callable):
    subtitles_path = {}

    for path, audio_path in audio_paths.items():
        srt_path = output_dir if output_srt else tempfile.gettempdir()
        srt_path = os.path.join(srt_path, f"{filename(path)}.srt")
        warnings.filterwarnings("ignore")
        result = transcribe(audio_path)
        warnings.filterwarnings("default")

        with open(srt_path, "w", encoding="utf-8") as srt:
            write_srt(result["segments"], file=srt)

        subtitles_path[path] = srt_path
    return srt_path


def download_youtube_video(url, path):
    yt = pytube.YouTube(url)

    # Trích xuất ID từ tiêu đề video
    video_id_match = re.search(r'([a-zA-Z0-9_-]+)\.mp4$', yt.title)
    if video_id_match:
        video_id = video_id_match.group(1)
    else:
        # Nếu không tìm thấy ID, sử dụng chuỗi ngẫu nhiên
        video_id = str(uuid.uuid4().hex)[:8]

    # Tạo tên file mới
    video_name = f"{video_id}.mp4"
    
    # Thêm đường dẫn đầy đủ
    video_path = os.path.join(path, video_name)
    
    stream = yt.streams.filter(file_extension='mp4').first()
    stream.download(output_path=path, filename=video_name)
    
    return video_path

# def download_youtube_video(url, path):
#     # Tạo thư mục nếu nó chưa tồn tại
#     os.makedirs(path, exist_ok=True)

#     # Tạo một ydl_opts để cấu hình tùy chọn tải xuống
#     ydl_opts = {
#         'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
#         'outtmpl': os.path.join(path, '%(title)s.%(ext)s')
#     }

#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         # Tải xuống video từ URL cung cấp
#         info_dict = ydl.extract_info(url, download=True)
#         video_title = info_dict.get('title', None)
#         if video_title:
#             # Xử lý tên video nếu cần
#             video_title = re.sub(r'[\/:*?"<>|]', '_', video_title)  # Loại bỏ các ký tự không hợp lệ trong tên tệp

#             # Đổi tên video tải xuống thành tên tiêu chuẩn
#             video_name = f"{video_title}.mp4"
#             downloaded_file = os.path.join(path, video_name)

#             # Kiểm tra nếu tệp đã tồn tại, nếu có, thêm một số duy nhất vào cuối
#             if os.path.isfile(downloaded_file):
#                 base, ext = os.path.splitext(downloaded_file)
#                 downloaded_file = f"{base}_{uuid.uuid4().hex[:8]}{ext}"

#             return downloaded_file
#         else:
#             return None  # Trả về None nếu không có thông tin về tiêu đề video

if __name__ == '__main__':
    result = main()
    print(json.dumps(result, indent=4))
from halo import Halo

spinner = Halo(text = 'Loading Document Models' , spinner='dots')
spinner.start()
from extractors.doc import txt_extractor , csv_extractor , pdf_extractor , ppt_extractor , doc_extractor
spinner.stop()

spinner = Halo(text = 'Loading Audio Models' , spinner='dots')
spinner.start()
from extractors.audio import aud_extractor
spinner.stop()

spinner = Halo(text = 'Loading Image Models' , spinner='dots')
spinner.start()
from extractors.image import img_extractor
spinner.stop()

spinner = Halo(text = 'Loading Video Models' , spinner='dots')
spinner.start()
from extractors.video import vid_extractor
spinner.stop()

class wrapper : 

    extraction_wrapper = {
        'txt' : lambda path : txt_extractor.txt_to_txt(path) , 
        'csv' : lambda path : csv_extractor.csv_to_txt(path) ,
        'mp4' : lambda path : vid_extractor.video_to_text(path) , 
        'mp3' : lambda path : aud_extractor.audio_to_text(path) , 
        'wav' : lambda path : aud_extractor.audio_to_text(path) , 
        'png' : lambda path : img_extractor.image_to_text(path) , 
        'jpg' : lambda path : img_extractor.image_to_text(path) , 
        'pptx' : lambda path : ppt_extractor.pptx_to_text(path) , 
        'docx' : lambda path : doc_extractor.docx_to_text(path) ,
        'pdf' : lambda path : pdf_extractor.pdf_to_text(path) ,  
        'jpeg' : lambda path : img_extractor.image_to_text(path) 
    }
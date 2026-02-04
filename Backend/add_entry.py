from os import path
import pandas as pd
from sanitise import *

def add_entry(id : str, medium : str, initialReleaseDate : str, titleEn : str, 
              titleRomaji = '', titleJp = '', triggerWarnings='',
              negativeRepresentations='',
              malID = '', thumbnail='Images/Thumbnails/placeholder.jpg'):
    csvPath = path.join('..','Data','tw_database.csv')
    
    data = {
        'id' : [sanitise(id)],
        'medium' : [sanitise(medium)],
        'initial_release_date' : [sanitise(initialReleaseDate)],
        'title_en' : [sanitise(titleEn)],
        'title_romaji' : [sanitise(titleRomaji)],
        'title_jp' : [sanitise(titleJp)],
        'trigger_warnings' : [sanitise(triggerWarnings)],
        'negative_representations' : [sanitise(negativeRepresentations)],
        'mal_id' : [sanitise(malID)],
        'thumbnail' : [sanitise(thumbnail)] 
    }

    df = pd.DataFrame(data)
    df.to_csv(csvPath, mode='a', index=False, header=False)

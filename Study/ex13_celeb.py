#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import json
import random

def recognize_celebrities(photo):
    celeb = ['조이현','신세경','박민영','송강','남주혁']
    
    client=boto3.client('rekognition')
    with open(photo, 'rb') as image:
        response = client.recognize_celebrities(Image={'Bytes': image.read()})

    print('Detected faces for ' + photo)
    
    if len(response['CelebrityFaces']) >= 1:
        for celebrity in response['CelebrityFaces']:
            print(f"닮은연예인은 {celebrity['Name']}입니다.")
    else:
       result=celeb[random.randint(0,4)]
       print(f"닮은연예인은 {result}입니다.")
    
    #print ('Name: ' + celebrity['Name'])
    #print ('Id: ' + celebrity['Id'])
    #print ('KnownGender: ' + celebrity['KnownGender'])
    #print ('Smile: ' + celebrity['Smile'])
    #print ('Position:')
    #print ('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
    #print ('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
    #print ('Info')
    #for url in celebrity['Urls']:
    #    print ('   ' + url)
    #print
    return len(response['CelebrityFaces'])

def main():
    photo='../../Downloads/jo.jpg'
    celeb_count=recognize_celebrities(photo)
    print("Celebrities detected: " + str(celeb_count))


if __name__ == "__main__":
    main()
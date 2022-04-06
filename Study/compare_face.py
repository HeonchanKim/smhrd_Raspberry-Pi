from flask import Flask, render_template
import os
import boto3
app = Flask(__name__)

def compare_faces():
    sourceFile = 'input.jpg'
    targetFile = '../../target.jpeg'
    
    client=boto3.client('rekognition')
    imageSource=open(sourceFile,'rb')
    imageTarget=open(targetFile,'rb')
    try:
        response=client.compare_faces(SimilarityThreshold=90,
                                      SourceImage={'Bytes': imageSource.read()},
                                      TargetImage={'Bytes': imageTarget.read()})
        
        for faceMatch in response['FaceMatches']:
            result = faceMatch['Similarity']
            
        imageSource.close()
        imageTarget.close()     
        return result
    except:
        return 0

@app.route('/')
def index():
    return render_template('main2.html')

@app.route('/detect')
def detect():
    os.system('raspistill -o input.jpg')
    result = compare_faces()
    return str(result)

if __name__ == "__main__":
    app.run()


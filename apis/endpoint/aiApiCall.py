from fastapi import APIRouter
from apis.model import aiModel
from transformers import pipeline
from transformers import AutoImageProcessor, AutoModelForImageClassification


model = pipeline("text-generation", model="gpt2")
classifier = pipeline('zero-shot-classification', model='roberta-large-mnli')
processor = AutoImageProcessor.from_pretrained("nateraw/food")
imgClassifier = AutoModelForImageClassification.from_pretrained("nateraw/food")
imgClassifier2 = pipeline("image-classification", model="nateraw/food")

router = APIRouter()


@router.post("/generate/")
def generate_text(item: aiModel.userInputParam):
    
    user_input = item.prompt

    action = ''

    result = model(item.prompt, max_length=item.max_length, num_return_sequences=1,truncation=True)
    response = result[0]["generated_text"]

    returnResult  = aiModel.aiRespose(response=response, action=action)

    return returnResult

@router.post("/generate2")
def generate_text(item: aiModel.userInputParam):
    
    
    sequence_to_classify = item.prompt
    action_labels = ['wave', 'eat', 'dancing', 'stay', 'jump', 'run']
    result = classifier(sequence_to_classify, action_labels)
    pp = 'do you want dance?'
    lables = result['labels']
    top_index = result['scores'].index(max(result['scores']))

    returnResult  = aiModel.aiRespose(response="OK", action=lables[top_index])

    return returnResult

@router.post("/classifyFoodImage")
def classify_food_image(item: aiModel.userInputParam):
    image = 'C:\jejuTourApi\spa.png'
    inputs = processor(image, return_tensors="pt")
    outputs = imgClassifier(**inputs)

    returnResult  = aiModel.aiRespose(response="OK", action=outputs)

    return returnResult

@router.post("/classifyFoodImage2")
def classify_food_image2(item: aiModel.userInputParam):
    image = 'C:\jejuTourApi\spa.png'
    
    outputs = imgClassifier2(image)
    print(outputs)

    returnResult  = aiModel.aiRespose(response="OK", action=outputs[0]['label'])

    return returnResult
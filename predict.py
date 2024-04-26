import torch
from functions import prediction
from transformers import DistilBertTokenizer
from model import DistillBERTClass
from torch import cuda

class PredictPipeline:
    def __init__(self) -> None:
        pass

    def predict(self, text):
        device = 'cuda' if cuda.is_available() else 'cpu'
        # model = load_object(os.path.join("artifacts","model_training","model.pkl"))
        model = DistillBERTClass()
        model.to(device)
        # Load the saved model weights into the initialized model
        model.load_state_dict(torch.load("model_state_dict_5.pth", map_location=torch.device('cpu')))

        # Make sure to set the model to evaluation mode after loading
        model.eval()
        tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-cased')
        result = prediction(model, tokenizer, device, text)
        # result = model.predict(text)
        if result == 0:
            result = "Human"
        else:
            result = "AI"
        
        return result


# Example usage
sentence = '''"America\'s love affair with it\'s vehicles seems to be cooling" says Elisabeth rosenthal. To understand rosenthal\'s perspective, it is easier to suggest that America\'s car usage is decreasing slowly. This isn\'t necessarily bad in the sense that it has certain positive effects. The advantages of limiting car usage includes an increase in security and health, along with a decrease in pollution and dependence.\n\nFirstly, when car usage is limited security and health is more likely to be guaranteed. The feeling of being secure is highly important to individuals everywhere. For example, many people in colombia used public transportation during a car free day "leaving the streets of this capital city ", according to Andrew Selsky, "eerily devoid of traffic jams". The complications that stem from traffic jams end with a feeling of confidence. The plan to get from point A to B was more simple just a second ago. This complication in your personal plans leads you to become stressed as a feeling of doubt overcomes all thoughts. If car usage was limited, there would be a control on how much traffic accumulates thus minimizing chance of stress. As Heidrun Walter states "when i had a car i was always tense. I\'m much happier this way". not only does car usage minimize conditions detrimental to health, it also enlarges your capacity for exercise. The main purpose of the car is to get someone from one place to another. when an important job takes over your personal life, it becomes difficult to do things most enjoyed in life. limits on car usage forces you to stay in shape. According to Andrew Selsky "parks and sports centers also have bloomed throughout the city". Less cars means healthier and natural situations. With parks and sport centers becoming more efficient, it becomes easier to find a more physically active population. Overall, less usage on cars minimizes stress and increases health.\n\nSecondly, limting car usage becomes beneficial to the environment. Now a days people have become annoyed with others who care so passionately about the environment. If you look behind their constant cries for action, there are solid facts. Yespollution is bad for the environment. Yes a bad envorment means unhealthy living. Yes cars are one of the main contributors to pollution in the environment. A pattern of less car usage, as Elisabeth Rosenthal states "will have beneficial implications for carbon emissions and the environment". The less use of cars, the less pollution in the environment. One must observe limiting car usage as an opportunity to create a cleaner world and better future. The effects of pollution in the environment is completley dangerous and we, the car users, are to blame.\n\nAdditionally, it would lower the dependence on cars. Many people today find that their car is so useful. While it has many features and is a form of transportation, many do not figure what they would do if they did not have such a possesion. The development of people and their interaction with technology has left a wide gap between historic, natural ways and what is thought of as modern society. Being dependent is not always good for individuals. As david goldberg says "all our development since world war II has been centered on the car, and that will have to change". Many people could disagree and wonder why it is necessary to change our ways especially if we are so highly devloped. If being developed means being dependent on a harmful machine, then it could not be effective devlopment. According to Elisabeth Rosenthal "cashstrapped americans could not afford new cars, and the unemployed were\'t going to work anyway". Many people can\'t have the precious luxury of private transportation in the first place. Those who have had it have become distant to a more natural society. Peope have become so use to having cars that they have become oblivious to the significant effects. With limits on car usage , these effcts could be controlled.\n\nTo conclude, the advantages of limiting car usage is an increase in health, along with a decrease in pollution, and less dependence on cars. limiting car usage is a positive way to enfore an organized and clean environment, and ensure health and security of those who live in it. This is one reason America can be reffered to as a succesful country. It is not that America has decreased use of vehicles, but the fact that they have done what is best for majority.'''


predictor = PredictPipeline()
print("Prediction:", predictor.predict(sentence))
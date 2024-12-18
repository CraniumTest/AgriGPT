from modules.data_processing import DataProcessor
from modules.language_model import AgriGPTInterface
from modules.image_recognition import ImageRecognition
from modules.iot_interface import IoTIntegration
from modules.market_analysis import MarketAnalyzer
from modules.recommendation_system import RecommendationEngine

def main():
    # Initialize modules
    data_processor = DataProcessor()
    agri_gpt = AgriGPTInterface()
    image_recog = ImageRecognition()
    iot_integration = IoTIntegration()
    market_analyzer = MarketAnalyzer()
    recommendation_engine = RecommendationEngine()
    
    # Example workflow
    weather_data = data_processor.get_weather_data()
    crop_advice = agri_gpt.get_crop_advice(weather_data)
    pest_detection = image_recog.detect_pests("crop_image.jpg")
    iot_data = iot_integration.get_equipment_data()
    market_info = market_analyzer.analyze_market()
    recommendations = recommendation_engine.generate_recommendations(weather_data, pest_detection, market_info)
    
    # Output results
    print(crop_advice)
    print(recommendations)

if __name__ == '__main__':
    main()

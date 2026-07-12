import pandas as pd
import numpy as np

def generate_mock_data():
    np.random.seed(42)
    n_samples = 200
    
    crops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas']
    data = []
    
    for _ in range(n_samples):
        crop = np.random.choice(crops)
        if crop == 'rice':
            data.append([np.random.uniform(60, 100), np.random.uniform(35, 60), np.random.uniform(35, 45), np.random.uniform(20, 27), np.random.uniform(80, 85), np.random.uniform(5, 7.5), np.random.uniform(150, 300), crop])
        elif crop == 'maize':
            data.append([np.random.uniform(60, 100), np.random.uniform(35, 60), np.random.uniform(15, 25), np.random.uniform(18, 27), np.random.uniform(50, 75), np.random.uniform(5.5, 7.5), np.random.uniform(60, 110), crop])
        elif crop == 'chickpea':
            data.append([np.random.uniform(20, 60), np.random.uniform(55, 80), np.random.uniform(75, 85), np.random.uniform(18, 20), np.random.uniform(14, 20), np.random.uniform(5.5, 8.5), np.random.uniform(60, 95), crop])
        elif crop == 'kidneybeans':
            data.append([np.random.uniform(10, 40), np.random.uniform(55, 80), np.random.uniform(15, 25), np.random.uniform(15, 25), np.random.uniform(18, 25), np.random.uniform(5.5, 6.0), np.random.uniform(60, 150), crop])
        elif crop == 'pigeonpeas':
            data.append([np.random.uniform(10, 40), np.random.uniform(55, 80), np.random.uniform(15, 25), np.random.uniform(18, 37), np.random.uniform(30, 70), np.random.uniform(4.5, 7.5), np.random.uniform(90, 200), crop])

    df = pd.DataFrame(data, columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'label'])
    df.to_csv('Crop_recommendation.csv', index=False)
    print("Mock dataset 'Crop_recommendation.csv' generated.")

if __name__ == '__main__':
    generate_mock_data()

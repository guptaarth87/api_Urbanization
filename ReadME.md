# Global Population Analysis API

### Project Overview

This project analyzes the population data of over 160 countries, providing insights into both urban and rural populations. It uses **Python** for the data analysis and **Flask** to create a RESTful API that allows users to easily access the population data. Additionally, a **Linear Regression** model is implemented to predict future population trends based on user input for specific years. This can help understand future rural and urban population distributions across the world.

---

## Features

1. **Population Data Access**:
   - Access data for over 160 countries, including the urban and rural population, total population, and respective percentages for different years.
   - Get data sorted by year, country, and urban/rural population percentage.

2. **Country-Specific Data**:
   - Retrieve the population details for any given country and year.
   
3. **Population Prediction**:
   - Use linear regression to predict the increase in urban population for any given country in future years.
   
4. **Flask API**:
   - Easy access to the dataset and predictions through a well-defined API structure.

---

## Technologies Used

- **Python**: For data analysis and machine learning.
- **Flask**: For creating the API.
- **Pandas**: For handling and manipulating data.
- **Scikit-learn**: To perform linear regression and make predictions.
- **CSV Data**: Urban and rural population data loaded from CSV files.

---

## API Endpoints

### 1. **Get Population Data**  
   **Endpoint**: `/data/`  
   **Method**: `GET`  
   **Description**: Retrieves the entire dataset, including rural and urban population data for all available countries.

### 2. **Get Country Names**  
   **Endpoint**: `/countryNames/`  
   **Method**: `GET`  
   **Description**: Returns a list of all distinct country names available in the dataset.

### 3. **Get Urban Population Data**  
   **Endpoint**: `/UrbanData/`  
   **Method**: `GET`  
   **Description**: Fetches urban population data for all countries.

### 4. **Get Rural Population Data**  
   **Endpoint**: `/ruralData/`  
   **Method**: `GET`  
   **Description**: Fetches rural population data for all countries.

### 5. **Get Development Ratio Data**  
   **Endpoint**: `/developmentRatio/`  
   **Method**: `GET`  
   **Description**: Returns data on the development ratio of urban versus rural areas.

### 6. **Urban Population Data By Year**  
   **Endpoint**: `/urbanisedDataByYear/<int:year>/`  
   **Method**: `GET`  
   **Description**: Provides the urban population data for a specified year, sorted in decreasing order by the urban population percentage.

### 7. **Rural Population Data By Year**  
   **Endpoint**: `/ruralDataByYear/<int:year>/`  
   **Method**: `GET`  
   **Description**: Provides the rural population data for a specified year, sorted in decreasing order by rural population percentage.

### 8. **Country Data By Date**  
   **Endpoint**: `/dataByDate/<string:country>/<int:year1>/`  
   **Method**: `GET`  
   **Description**: Returns detailed population data for a specific country and year.

### 9. **Population Prediction**  
   **Endpoint**: `/predict/<string:country>`  
   **Method**: `GET`  
   **Description**: Predicts future urban population trends for a specific country using linear regression. Returns predicted values for future years along with the model's accuracy score.

---

## How to Use

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/population-analysis-api.git
cd population-analysis-api
```

### 2. Install required dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask Application
```bash
python app.py
```

### 4. Access the API
Once the application is running, you can access the API at `http://localhost:5000/`.

---

## Example API Request and Response

### **Request**: Urban Population Data By Year
```bash
GET /urbanisedDataByYear/2020/
```

### **Response**:
```json
{
  "sorted_urban_dataset": [
    {
      "Country1": {
        "Urban_population": 5000000,
        "Code": "C1",
        "Year": 2020,
        "Rural_population": 2000000,
        "Total_Population": 7000000,
        "Urban_Population_percentage": 71.43
      }
    },
    ...
  ],
  "status": 200
}
```

---

## Future Enhancements

- Add more prediction models for rural population analysis.
- Create visualization tools to better represent the trends and patterns in the population data.
- Extend the API to allow user-defined queries for more customized results.

---

## License
This project is licensed under the MIT License.

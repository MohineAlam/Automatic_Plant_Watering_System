This version of the automatic watering system implements a decision tree ml model. This system uses collected humidty and watering data to train the ml to learn when to water your plant.
Using the GUI, create a 'plant diary' json file which is populated with the plant name, humidty value of days watered and not watered.
Feed this diary into the ml and predict if the plant needs watering today.

```mermaid
flowchart TD

		subgraph Data Collection
			A1[Plant name]
			A2[Date]
			A3[Humidity of soil]
			A4[If watered: Date watered]
			A5[If watered: Humidity of wet soil]
		end

		subgraph Model Training
			B1[Train ml - Manual humidity threshold provided once]
		end

		subgraph Prediction
			C1[Model predicts if plant needs watering]
		end

		subgraph Future System
			D1[ not available currently - integration into automatic watering system ]
		end

		A1 --> B1
		A2 --> B1
		A3 --> B1
		A4 --> B1
		A5 --> B1
		B1 --> C1 --> D1
```
		

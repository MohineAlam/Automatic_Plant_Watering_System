This version of the automatic watering system implements a decision tree ml model. This system uses collected humidty and watering data to train the ml to learn when to water your plant.
Using the GUI, create a 'plant diary' json file which is populated with the plant name, humidty value of days watered and not watered.
Feed this diary into the ml and predict if the plant needs watering today.

```mermaid
	flowchart TD

		subgraph Data Collection
			A --> A1[Plant name]
			A --> A2[Date]
			A --> A3[Humidity of soil]
			A --> A4[If watered: Date watered]
			A --> A5[If watered: Humidty of wet soil]
		end

		subgraph Model Training
			B --> B1[Train ml (Manual humidty threshold provided once)]
		end

		subgraph Prediction
			C --> C1[Model predicts if plant needs watering]
		end

		subgraph Future System
			D --> D1[ (not available currently) integration into automatic watering system ]
		end

		A1 --> B1
		A2 --> B1
		A3 --> B1
		A4 --> B1
		A5 --> B1
		B1 --> C1 --> D1
```
		

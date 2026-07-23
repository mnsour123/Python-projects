# BMI Calculator

A simple desktop BMI (Body Mass Index) calculator built with Python's `tkinter` library.

## Features

- Clean, simple GUI built with `ttk` widgets
- Calculates BMI from weight (kg) and height (cm)
- Displays BMI category: Underweight, Normal weight, Overweight, or Obese
- Input validation with error messages for invalid or empty input
- Clear button to reset the form

## Requirements

- Python 3.x
- `tkinter` (included with most standard Python installations)

No external dependencies or `pip install` needed.

## How to Run

1. Save the code as `bmi_calculator.py`
2. Run it from your terminal:

```bash
python bmi_calculator.py
```

## Usage

1. Enter your weight in kilograms (kg)
2. Enter your height in centimeters (cm)
3. Click **Calculate** to see your BMI and category
4. Click **Clear** to reset the fields and try again

## BMI Categories

| BMI Range   | Category      |
| ----------- | ------------- |
| Below 18.5  | Underweight   |
| 18.5 – 24.9 | Normal weight |
| 25.0 – 29.9 | Overweight    |
| 30.0 and up | Obese         |

## Formula

```
BMI = weight (kg) / (height (m))^2
```

## Possible Improvements

- Add a BMI history log
- Add a colored progress bar/indicator based on category
- Support imperial units (lbs/inches)
- Save results to a file (CSV/JSON)

## License

Free to use and modify for personal or educational purposes.

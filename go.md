
You're an expert that processes video captions and returns specific segments of text along with their start time and duration. You are required to return a json formate of it for duration less than 1 minute for {number} of shorts
from the all captions that follow these instructions {instructions}

some examples here are:
Certainly! Here's an example of captions and the expected output for each content type:

example 1:
**Captions:**

captions = [
    {"start": 0, "duration": 3, "text": "Did you know that the honeybee is the only insect that produces food eaten by humans?"},
    {"start": 5, "duration": 4, "text": "The shortest war in history lasted only 38 minutes between Britain and Zanzibar in 1896."},
    {"start": 10, "duration": 5, "text": "In 2006, an Australian man tried to sell New Zealand on eBay. The starting price was $0.01."}
]
```

**Expected output for "facts"**:
```json
[
    {"start": 0, "duration": 12, "text": "Did you know that the honeybee is the only insect that produces food eaten by humans? The shortest war in history lasted only 38 minutes between Britain and Zanzibar in 1896. In 2006, an Australian man tried to sell New Zealand on eBay. The starting price was $0.01."}
]
```

**Expected output for "quotes"**:
```json
[]
```
example 2:
Certainly! Here are some example captions and their expected outputs based on different content types:

### Example Captions:

```python
captions = [
    {"start": 0, "duration": 4, "text": "The Eiffel Tower was completed in 1889."},
    {"start": 5, "duration": 3, "text": "Ants don't sleep."},
    {"start": 10, "duration": 5, "text": "The Earth's atmosphere is composed of 78% nitrogen."},
    {"start": 18, "duration": 3, "text": "The Great Wall of China is over 13,000 miles long."},
    {"start": 23, "duration": 4, "text": "Elephants are the only mammals that can't jump."},
]

```

### Expected Outputs:

1. **Facts**:
   - Instructions: `"content_type": "facts"`
   - Expected Output:
     ```json
     [
         {"start": 0, "duration": 4, "text": "The Eiffel Tower was completed in 1889.Ants don't sleep.The Earth's atmosphere is composed of 78% nitrogen.The Great Wall of China is over 13,000 miles long.Elephants are the only mammals that can't jump."}
     ]
     ```

2. **Quotes**:
   - Instructions: `"content_type": "quotes"`
   - Expected Output:
     ```json
     []
     ```

3. **Science**:
   - Instructions: `"content_type": "science"`
   - Expected Output:
     ```json
     [
         {"start": 10, "duration": 5, "text": "The Earth's atmosphere is composed of 78% nitrogen."}
     ]
     ```

4. **History**:
   - Instructions: `"content_type": "history"`
   - Expected Output:
     ```json
     [
         {"start": 0, "duration": 4, "text": "The Eiffel Tower was completed in 1889."},
         {"start": 18, "duration": 3, "text": "The Great Wall of China is over 13,000 miles long."}
     ]
     ```

5. **Animals**:
   - Instructions: `"content_type": "animals"`
   - Expected Output:
     ```json
     [
         {"start": 23, "duration": 4, "text": "Elephants are the only mammals that can't jump."}
     ]
     ```




//////////////////////////////////////////////////////////////////////////////
-----------------------------------------------------------------------------
//////////////////////////////////////////////////////////////////////////////



You're an expert tasked with processing video captions and returning specific segments of text along with their start time and duration. You need to generate a JSON format for captions with a duration less than one minute for a specified number of shorts, following given instructions.

Here are some examples:

**Example 1:**

**Captions:**

```python
captions = [
    {"start": 0, "duration": 3, "text": "Did you know that the honeybee is the only insect that produces food eaten by humans?"},
    {"start": 5, "duration": 4, "text": "The shortest war in history lasted only 38 minutes between Britain and Zanzibar in 1896."},
    {"start": 10, "duration": 5, "text": "In 2006, an Australian man tried to sell New Zealand on eBay. The starting price was $0.01."}
]
```

**Expected Output for "facts"**:
```json
[
    {"start": 0, "duration": 12, "text": "Did you know that the honeybee is the only insect that produces food eaten by humans? The shortest war in history lasted only 38 minutes between Britain and Zanzibar in 1896. In 2006, an Australian man tried to sell New Zealand on eBay. The starting price was $0.01."}
]
```

**Expected Output for "quotes"**:
```json
[]
```

**Example 2:**

**Captions:**

```python
captions = [
    {"start": 0, "duration": 4, "text": "The Eiffel Tower was completed in 1889."},
    {"start": 5, "duration": 3, "text": "Ants don't sleep."},
    {"start": 10, "duration": 5, "text": "The Earth's atmosphere is composed of 78% nitrogen."},
    {"start": 18, "duration": 3, "text": "The Great Wall of China is over 13,000 miles long."},
    {"start": 23, "duration": 4, "text": "Elephants are the only mammals that can't jump."},
]
```

**Expected Outputs:**

1. **Facts**:
   - Instructions: `"content_type": "facts"`
   - Expected Output:
     ```json
     [
         {"start": 0, "duration": 4, "text": "The Eiffel Tower was completed in 1889.Ants don't sleep.The Earth's atmosphere is composed of 78% nitrogen.The Great Wall of China is over 13,000 miles long.Elephants are the only mammals that can't jump."}
     ]
     ```

2. **Quotes**:
   - Instructions: `"content_type": "quotes"`
   - Expected Output:
     ```json
     []
     ```

3. **Science**:
   - Instructions: `"content_type": "science"`
   - Expected Output:
     ```json
     [
         {"start": 10, "duration": 5, "text": "The Earth's atmosphere is composed of 78% nitrogen."}
     ]
     ```

4. **History**:
   - Instructions: `"content_type": "history"`
   - Expected Output:
     ```json
     [
         {"start": 0, "duration": 4, "text": "The Eiffel Tower was completed in 1889."},
         {"start": 18, "duration": 3, "text": "The Great Wall of China is over 13,000 miles long."}
     ]
     ```

5. **Animals**:
   - Instructions: `"content_type": "animals"`
   - Expected Output:
     ```json
     [
         {"start": 23, "duration": 4, "text": "Elephants are the only mammals that can't jump."}
     ]
     ```

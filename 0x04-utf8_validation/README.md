# 0x04-utf8_validation
### CONTENT
1. [What is UTF-8?](#what-is-utf-8)
2. [How does it work?](#how-does-it-work)
3. [Making a function that checks if a list is a valid UTF-8 encoding.](#solving-the-task)

### WHAT IS UTF-8
It is called the miracle used in computing and the internet for encoding text. It is capable of representing any character from any language, making it universally accepted as an international standard.

ASCII is a great standard that encodes numbers in binary and hexadecimal and letters as well, as even special characters, which is great. But that was only valid for the Latin world. For the rest of the world, there are other alphabets to include, imagine Arabic, Chinese, and Korean...
These countries had to come up with an encoding of their own.

In circumstances where different countries have different encodings imagine what would the communication between them be like. What would look just fine on a computer would look like gibberish on the other.

The UTF-8 came to put an end to this. It has more than a hundred thousand characters that cover all you would write in any possible language.

### HOW DOES IT WORK

The UTF-8 represents each character in the Unicode character using a variable number of bytes. When working with characters in the range 0 to 127 the ASCII code will still be valid. But characters outside the ASCII range will be represented using multiple bytes, and the number of bytes required depends on the Unicode point of the character.

Here is a representation taken from a video on YouTube by **Computerphile**.<br>
Link : [Characters, Symbols and the Unicode Miracle - Computerphile](https://www.youtube.com/watch?v=MijmeoH9LT4)

![How does UTF-8 work?](/0x04-utf8_validation/Pictues/INTERVIEW_diagram_UTF-8.png)
### SOLVING THE TASK

We will be making a function that takes input data in the form of a list of integers, and returns True in case data is a valid UTF-8 encoding and False otherwise.

Our code will be grouped in a try-except block because we will be returning False when the exception **UnicodeDecodeError** rises.

The idea is to loop through integers in the list and transform the integer into its binary representation. The bitwise operation between the integers and 0xFF is necessary to keep the number of bits in check, that way if the bits are more than 8 bits then the function won't result in a traceback with a value error.

After the data is transformed to bytes now it's time to decode it using utf-8 standard. If everything went well the function will return True, but if an exception was raised the function will return False.

```python
def validUTF8(data):
    """A method that determines if a given data set
    represents a valid UTF-8 encoding."""
    try:
        data = bytes(i & 0xFF for i in data)
        data.decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False
```

import tensorflow as tf
model = "runs/train/exp9/weights/best-fp16.tflite" 
interpreter = tf.lite.Interpreter(model_path = model) 
print(interpreter.get_input_details()) 
print(interpreter.get_output_details())  

# 'shape': array([  1, 640, 640,   3])
# 'shape': array([    1, 25200,     7])
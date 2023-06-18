import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(32, activation='relu', input_shape=(32,)),
    keras.layers.Dense(32, activation='relu'),  
    keras.layers.Dense(16, activation='relu'),  
    keras.layers.Dense(13, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=20, batch_size=32)
loss, accuracy = model.evaluate(x_test, y_test)

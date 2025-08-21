from keras.models import Sequential
from keras.layers import Dense

# Dummy model (just for testing FastAPI)
model = Sequential([
    Dense(64, activation='relu', input_shape=(100,)),  # input shape: 100 features
    Dense(10, activation='softmax')                    # output: 10 classes
])

# Compile
model.compile(optimizer="adam", loss="categorical_crossentropy")

# Save dummy model
model.save("model_weights.h5")

print("✅ Dummy model saved as model_weights.h5")

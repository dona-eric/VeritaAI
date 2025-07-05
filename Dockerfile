FROM python:3.10

# Set the working directory
WORKDIR /app
# make copy the requirements file

COPY requirements.txt ./

# Install the dependencies
RUN pip install --upgrade pip
# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
COPY start.sh /start.sh
RUN chmod +x /start.sh

# load the environment variables
ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD [ "/start.sh" ]


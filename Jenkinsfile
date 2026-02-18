pipeline {
    agent any

    environment {
        // You should configure these credentials in Jenkins
        // DEPLOY_SERVER = 'ec2-user@your-ec2-ip' 
        // SSH_KEY = credentials('ec2-ssh-key') 
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    # Run tests here if you have them. 
                    # For now, we just check if app.py exists
                    ls -l app.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                // This stage assumes you have set up SSH access to your EC2 instance
                // and added the SSH key to Jenkins credentials.
                // Replace 'your-ec2-ip' and 'ec2-user' with your actual details in the environment section or directly here.
                
                sshagent(['ec2-ssh-key']) {
                   sh '''
                       # Prepare the remote directory
                       ssh -o StrictHostKeyChecking=no ec2-user@your-ec2-ip "mkdir -p ~/calculator-app"
                       
                       # Copy files to EC2
                       scp -o StrictHostKeyChecking=no -r ./* ec2-user@your-ec2-ip:~/calculator-app
                       
                       # Install dependencies and restart service on EC2
                       ssh -o StrictHostKeyChecking=no ec2-user@your-ec2-ip "
                           cd ~/calculator-app
                           python3 -m venv venv
                           . venv/bin/activate
                           pip install -r requirements.txt
                           # Assuming you have a systemd service set up, restart it
                           # sudo systemctl restart calculator-app
                           # OR for simple testing, kill old process and start new one (not recommended for production)
                           # pkill -f gunicorn || true
                           # nohup gunicorn -w 4 -b 0.0.0.0:5000 app:app > app.log 2>&1 &
                       "
                   '''
                }
            }
        }
    }
}

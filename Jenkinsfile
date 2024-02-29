pipeline{
    agent any
    stages{
        stage("Setting the virtual environment"){
            steps
            {
                sh '''
                chmod +x envsetup.sh
                ./envsetup.sh
                '''
            }
        }
        stage("Gunicon Setup"){
            steps
            {
                sh '''
                chmod +x gunicorn.sh
                ./gunicorn.sh
                '''
            }
        }
        stage("NGINX Setup"){
            steps
            {
                sh '''
                chmod +x nginx.sh
                ./nginx.sh
                '''
            }
        }
    }
}
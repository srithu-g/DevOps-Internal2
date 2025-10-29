pipeline { 
    agent any 
    stages { 
        stage('Build') { 
            steps { 
                echo "Build Docker Image" 
                bat "docker build -t demoapp ."
            } 
        } 
        stage('Run') { 
            steps { 
                echo "Run application in Docker Container" 
                bat "docker rm -f mycontainer || exit 0" 
                bat "docker run -d -p 5000:5000 --name mycontainer demoapp" 
                
            } 
        } 
    } 
    post { 
        success { 
            echo 'Pipeline completed successfully!' 
        } 
        failure { 
            echo 'Pipeline failed.' 
        } 
    } 
}

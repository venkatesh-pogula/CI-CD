pipeline{
    agent { label 'GOL'}
    triggers{
        cron('H * * * *')
        pollSCM('* * * * *')
    }
    parameters{
        string (name: 'BRANCH' , defaultValue: 'game-of-file' , description: 'this is setting varibale or parameter for branch')
    }
    stages{
        stage ('scm') {
            steps{
            git branch: "${params.BRANCH}", url: 'https://github.com/venkatesh-pogula/CI-CD.git'
            }
        }
        stage ('build') {
            steps{
                
                sh 'mvn package'
            }
            
        }
    }
    post{
        success {
            archive '**/gameoflife.war'
            junit '**/TEST-*.xml'

        }
    }
}
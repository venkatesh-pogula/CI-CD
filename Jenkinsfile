pipeline{
    agent { label 'GOL'}
    triggers{
        cron('H * * * *')
        pollSCM('* * * * *')
    }
    parameters{
        string (name: 'BRANCH' , defaultValue: 'game-of-file' , description: 'this is setting varibale or parameter for branch')
        choice(name: 'GOAL', choices: ['package', 'clean package', 'install'], description: 'maven golas')
    }
    // global environment  variable
    environment{
        CI_ENV = 'Pogula'
    }

    stages{
        stage ('scm') {
            // stages enviroment variables
            environment {
                DUMMY = 'venkatesh'
            }
            steps{
            git branch: "${params.BRANCH}", url: 'https://github.com/venkatesh-pogula/CI-CD.git'
            echo env.DUMMY // it will print the dummy value as venkatesh
            echo env.CI_ENV // it will print the value global variable 
            }
        }
        stage ('build') {
            steps{
                echo env.GIT_URL // it will print the value of git url
                sh "mvn ${params.GOAL}" // it will excuete the choices any one
            }
            stash name: 'golwar' includes: '**/gameoflife.war'
        }
        stage('deploy'){
            agent (label 'ANSIBLE')
            steps{
                  unstash name: 'golwar' 
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
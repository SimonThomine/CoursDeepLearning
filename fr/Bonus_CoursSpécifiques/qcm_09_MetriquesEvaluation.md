# QCM Interactif
```{raw} html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QCM Interactif</title>
    
    <!-- Ajout de MathJax pour les équations LaTeX -->
    <script type="text/javascript" id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">
    </script>
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['\\(', '\\)'], ['$', '$']],
                displayMath: [['\\[', '\\]'], ['$$', '$$']]
            }
        };
    </script>
    
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            min-height: 100vh;
            padding: 2rem 1rem;
            line-height: 1.6;
        }

        .header {
            text-align: center;
            margin-bottom: 3rem;
            color: white;
        }

        .header h1 {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        .header p {
            font-size: 1.1rem;
            opacity: 0.9;
            font-weight: 300;
        }

        .qcm-container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
            position: relative;
        }

        .qcm-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 6px;
            background: linear-gradient(90deg, #667eea, #764ba2);
        }

        .question-container {
            padding: 2rem;
            border-bottom: 1px solid #f0f0f0;
            transition: all 0.3s ease;
        }

        .question-container:last-child {
            border-bottom: none;
        }

        .question-header {
            display: flex;
            align-items: center;
            margin-bottom: 1.5rem;
        }

        .question-number {
            background: linear-gradient(135deg, #636e72, #2d3436);
            color: white;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            margin-right: 1rem;
            flex-shrink: 0;
        }

        .question-text {
            font-size: 1.1rem;
            color: #2d3748;
            font-weight: 500;
            flex: 1;
        }

        .answers {
            display: grid;
            gap: 0.8rem;
        }

        .answer-button {
            display: flex;
            align-items: center;
            width: 100%;
            padding: 1rem 1.2rem;
            background: #f8f9fa;
            border: 2px solid #e9ecef;
            border-radius: 12px;
            font-size: 1rem;
            color: #495057;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: left;
            position: relative;
            overflow: hidden;
        }

        .answer-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: left 0.5s;
        }

        .answer-button:hover::before {
            left: 100%;
        }

        .answer-button:hover {
            background: #e3f2fd;
            border-color: #2196f3;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(33, 150, 243, 0.2);
        }

        .answer-option {
            background: #636e72;
            color: white;
            width: 28px;
            height: 28px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            margin-right: 0.8rem;
            flex-shrink: 0;
            font-size: 0.9rem;
        }

        .answer-text {
            flex: 1;
        }

        .answer-button.correct {
            background: linear-gradient(135deg, #48bb78, #38a169);
            border-color: #38a169;
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(72, 187, 120, 0.3);
        }

        .answer-button.correct .answer-option {
            background: rgba(255,255,255,0.2);
        }

        .answer-button.incorrect {
            background: linear-gradient(135deg, #f56565, #e53e3e);
            border-color: #e53e3e;
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(245, 101, 101, 0.3);
        }

        .answer-button.incorrect .answer-option {
            background: rgba(255,255,255,0.2);
        }

        .answer-button.show-correct {
            background: linear-gradient(135deg, #4299e1, #3182ce);
            border-color: #3182ce;
            color: white;
            animation: highlight 1s ease;
        }

        .answer-button.show-correct .answer-option {
            background: rgba(255,255,255,0.2);
        }

        @keyframes highlight {
            0%, 100% { transform: translateY(-2px); }
            50% { transform: translateY(-4px); }
        }

        .answer-button:disabled {
            cursor: not-allowed;
        }

        .feedback {
            margin-top: 1rem;
            padding: 1rem;
            border-radius: 12px;
            font-weight: 500;
            display: flex;
            align-items: center;
            animation: slideIn 0.3s ease;
        }

        @keyframes slideIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .feedback.correct {
            background: linear-gradient(135deg, #c6f6d5, #9ae6b4);
            color: #22543d;
        }

        .feedback.incorrect {
            background: linear-gradient(135deg, #fed7d7, #feb2b2);
            color: #742a2a;
        }

        .feedback-icon {
            margin-right: 0.5rem;
            font-size: 1.2rem;
        }

        .progress-bar {
            position: fixed;
            top: 0;
            left: 0;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            transition: width 0.3s ease;
            z-index: 1000;
        }

        .score-container {
            background: linear-gradient(135deg, #f7fafc, #edf2f7);
            padding: 2rem;
            text-align: center;
            border-top: 1px solid #e2e8f0;
        }

        .score-text {
            font-size: 1.2rem;
            color: #2d3748;
            font-weight: 600;
        }

        /* Styles pour le formatage Markdown améliorés */
        em {
            font-style: italic;
            color: inherit;
            font-weight: 500;
        }

        strong {
            font-weight: 700;
            color: #2d3748;
        }

        code {
            background: linear-gradient(135deg, #f1f5f9, #e2e8f0);
            padding: 0.2rem 0.4rem;
            border-radius: 6px;
            font-family: 'JetBrains Mono', 'Fira Code', monospace;
            font-size: 0.9em;
            color: #667eea;
            border: 1px solid #e2e8f0;
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .qcm-container {
                margin: 0;
                border-radius: 0;
            }
            
            .question-container {
                padding: 1.5rem;
            }
            
            .header h1 {
                font-size: 2rem;
            }
        }
        .navigation-bar {
            position: fixed;
            top: 20px;
            left: 20px;
            z-index: 1001;
        }

        .back-to-course-btn {
            background: rgba(255, 255, 255, 0.95);
            color: #2c3e50;
            border: 2px solid rgba(44, 62, 80, 0.2);
            padding: 12px 20px;
            border-radius: 25px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
            font-size: 14px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .back-to-course-btn:hover {
            background: rgba(44, 62, 80, 0.9);
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
        }

        .back-to-course-btn i {
            font-size: 12px;
        }

        @media (max-width: 768px) {
            .navigation-bar {
                top: 10px;
                left: 10px;
            }
            
            .back-to-course-btn {
                padding: 10px 16px;
                font-size: 13px;
            }
        }
    </style>
</head>
<body>
<div class="navigation-bar">
    <button class="back-to-course-btn" onclick="goBackToCourse()">
        <i class="fas fa-arrow-left"></i> Retour aux cours
    </button>
</div>
<div class="progress-bar" id="progressBar"></div>

<div class="header">
    <h1><i class="fas fa-brain"></i> QCM Interactif</h1>
    <p>Testez vos connaissances !</p>
</div>

<div class="qcm-container">
    
        <div class="question-container">
            <div class="question-header">
                <div class="question-number">1</div>
                <div class="question-text">Dans une classification binaire, comment définit-on la précision ?  </div>
            </div>
            <div class="answers">
        
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 1)" data-question="1">
                    <div class="answer-option">A</div>
                    <div class="answer-text">Le nombre d’éléments positifs correctement classés divisé par le nombre total d’éléments positifs réels</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, true, 'B', 1)" data-question="1">
                    <div class="answer-option">B</div>
                    <div class="answer-text">Le nombre d’éléments positifs correctement classés divisé par le nombre total d’éléments classés positifs par le modèle</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 1)" data-question="1">
                    <div class="answer-option">C</div>
                    <div class="answer-text">Le nombre d’éléments négatifs correctement classés divisé par le nombre total d’éléments négatifs réels</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 1)" data-question="1">
                    <div class="answer-option">D</div>
                    <div class="answer-text">Le nombre total de prédictions correctes divisé par le nombre total de prédictions</div>
                </button>
            
            </div>
        </div>
        
        <div class="question-container">
            <div class="question-header">
                <div class="question-number">2</div>
                <div class="question-text">Quelle métrique est définie comme la moyenne harmonique entre la précision et le rappel ?  </div>
            </div>
            <div class="answers">
        
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 2)" data-question="2">
                    <div class="answer-option">A</div>
                    <div class="answer-text">Accuracy</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, true, 'B', 2)" data-question="2">
                    <div class="answer-option">B</div>
                    <div class="answer-text">F1-score</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 2)" data-question="2">
                    <div class="answer-option">C</div>
                    <div class="answer-text">Specificité</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 2)" data-question="2">
                    <div class="answer-option">D</div>
                    <div class="answer-text">Average Precision (AP)</div>
                </button>
            
            </div>
        </div>
        
        <div class="question-container">
            <div class="question-header">
                <div class="question-number">3</div>
                <div class="question-text">Quel est l’axe des abscisses (X) dans la courbe ROC ?  </div>
            </div>
            <div class="answers">
        
                <button class="answer-button" onclick="checkAnswer(this, false, 'C', 3)" data-question="3">
                    <div class="answer-option">A</div>
                    <div class="answer-text">Le taux de vrais positifs (rappel)</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'C', 3)" data-question="3">
                    <div class="answer-option">B</div>
                    <div class="answer-text">Le taux de faux négatifs</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, true, 'C', 3)" data-question="3">
                    <div class="answer-option">C</div>
                    <div class="answer-text">Le taux de faux positifs (1 - spécificité)</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'C', 3)" data-question="3">
                    <div class="answer-option">D</div>
                    <div class="answer-text">La précision</div>
                </button>
            
            </div>
        </div>
        
        <div class="question-container">
            <div class="question-header">
                <div class="question-number">4</div>
                <div class="question-text">Quelle métrique est la moyenne des carrés des erreurs entre valeurs prédites et valeurs réelles ?  </div>
            </div>
            <div class="answers">
        
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 4)" data-question="4">
                    <div class="answer-option">A</div>
                    <div class="answer-text">Mean Absolute Error (MAE)</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, true, 'B', 4)" data-question="4">
                    <div class="answer-option">B</div>
                    <div class="answer-text">Mean Squared Error (MSE)</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 4)" data-question="4">
                    <div class="answer-option">C</div>
                    <div class="answer-text">Intersection Over Union (IoU)</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 4)" data-question="4">
                    <div class="answer-option">D</div>
                    <div class="answer-text">Log loss</div>
                </button>
            
            </div>
        </div>
        
        <div class="question-container">
            <div class="question-header">
                <div class="question-number">5</div>
                <div class="question-text">Dans une tâche de segmentation, quelle métrique est plus adaptée que l’IoU pour réduire le biais envers les petits objets et classes rares ?  </div>
            </div>
            <div class="answers">
        
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 5)" data-question="5">
                    <div class="answer-option">A</div>
                    <div class="answer-text">Average Precision (AP)</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, true, 'B', 5)" data-question="5">
                    <div class="answer-option">B</div>
                    <div class="answer-text">Dice Coefficient</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 5)" data-question="5">
                    <div class="answer-option">C</div>
                    <div class="answer-text">F1-score</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 5)" data-question="5">
                    <div class="answer-option">D</div>
                    <div class="answer-text">Recall</div>
                </button>
            
            </div>
        </div>
        
    <div class="score-container">
        <div class="score-text" id="scoreDisplay">Score: 0/5</div>
    </div>
</div>

<script>
    let totalQuestions = 5;
    let answeredQuestions = 0;
    let correctAnswers = 0;

    function updateProgress() {
        const progress = (answeredQuestions / totalQuestions) * 100;
        document.getElementById('progressBar').style.width = progress + '%';
    }

    function updateScore() {
        document.getElementById('scoreDisplay').innerHTML = `Score: ${correctAnswers}/${totalQuestions}`;
    }

    function goBackToCourse() {
        // Essaie d'utiliser l'historique du navigateur
        if (document.referrer && document.referrer.includes(window.location.hostname)) {
            window.history.back();
        } else {
            // Sinon, redirige vers l'index du chapitre
            window.location.href = './';
        }
    }

    function checkAnswer(button, isCorrect, correctAnswer, questionNumber) {
        // Désactiver tous les boutons de cette question
        const questionContainer = button.closest('.question-container');
        const buttons = questionContainer.querySelectorAll('.answer-button');
        
        buttons.forEach(btn => {
            btn.disabled = true;
        });

        // Incrémenter les questions répondues si c'est la première fois
        if (!button.hasAttribute('data-answered')) {
            answeredQuestions++;
            button.setAttribute('data-answered', 'true');
        }

        let feedbackHtml = '';
        
        if (isCorrect) {
            button.classList.add('correct');
            correctAnswers++;
            feedbackHtml = `
                <div class="feedback correct">
                    <i class="fas fa-check-circle feedback-icon"></i>
                    Excellent ! Vous avez trouvé la bonne réponse.
                </div>
            `;
        } else {
            button.classList.add('incorrect');
            
            // Trouver et mettre en surbrillance la bonne réponse
            buttons.forEach(btn => {
                const optionText = btn.querySelector('.answer-text').textContent;
                const optionLetter = btn.querySelector('.answer-option').textContent;
                if ((optionLetter + ') ' + optionText).startsWith(correctAnswer)) {
                    btn.classList.add('show-correct');
                }
            });
            
            feedbackHtml = `
                <div class="feedback incorrect">
                    <i class="fas fa-times-circle feedback-icon"></i>
                    Incorrect ! La bonne réponse était : <strong>${correctAnswer}</strong>
                </div>
            `;
        }

        // Ajouter le feedback s'il n'existe pas déjà
        if (!questionContainer.querySelector('.feedback')) {
            questionContainer.insertAdjacentHTML('beforeend', feedbackHtml);
        }

        updateProgress();
        updateScore();
        
        // Re-render MathJax après modification du contenu
        if (window.MathJax) {
            MathJax.typesetPromise([questionContainer]).then(() => {
                console.log('MathJax re-rendered');
            }).catch((err) => console.log(err.message));
        }
    }

    // Animation d'entrée pour les questions
    document.addEventListener('DOMContentLoaded', function() {
        const questions = document.querySelectorAll('.question-container');
        questions.forEach((question, index) => {
            question.style.opacity = '0';
            question.style.transform = 'translateY(20px)';
            setTimeout(() => {
                question.style.transition = 'all 0.5s ease';
                question.style.opacity = '1';
                question.style.transform = 'translateY(0)';
            }, index * 100);
        });
    });
</script>
    
</body>
</html>
```
    
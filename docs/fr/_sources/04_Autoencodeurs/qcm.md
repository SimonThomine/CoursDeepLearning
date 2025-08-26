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
                <div class="question-text">Quelle est la principale différence entre l'apprentissage supervisé et non supervisé ?  </div>
            </div>
            <div class="answers">
        
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 1)" data-question="1">
                    <div class="answer-option">A</div>
                    <div class="answer-text">L'apprentissage supervisé utilise uniquement des données non étiquetées, tandis que l'apprentissage non supervisé utilise des données étiquetées.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, true, 'B', 1)" data-question="1">
                    <div class="answer-option">B</div>
                    <div class="answer-text">L'apprentissage supervisé utilise des données étiquetées (x et y), tandis que l'apprentissage non supervisé utilise uniquement des données d'entrée (x) sans sortie associée.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 1)" data-question="1">
                    <div class="answer-option">C</div>
                    <div class="answer-text">L'apprentissage supervisé ne peut pas être utilisé pour la détection d'anomalies, contrairement à l'apprentissage non supervisé.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 1)" data-question="1">
                    <div class="answer-option">D</div>
                    <div class="answer-text">L'apprentissage supervisé est toujours plus rapide que l'apprentissage non supervisé.</div>
                </button>
            
            </div>
        </div>
        
        <div class="question-container">
            <div class="question-header">
                <div class="question-number">2</div>
                <div class="question-text">Quel est l'objectif principal d'un autoencodeur dans le contexte de la détection d'anomalies non supervisée ?  </div>
            </div>
            <div class="answers">
        
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 2)" data-question="2">
                    <div class="answer-option">A</div>
                    <div class="answer-text">Prédire explicitement les labels des données d'entrée.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, true, 'B', 2)" data-question="2">
                    <div class="answer-option">B</div>
                    <div class="answer-text">Compresser les données d'entrée et les reconstruire pour détecter les différences entre données normales et anormales.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 2)" data-question="2">
                    <div class="answer-option">C</div>
                    <div class="answer-text">Classifier les données en différentes catégories.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 2)" data-question="2">
                    <div class="answer-option">D</div>
                    <div class="answer-text">Générer de nouvelles données synthétiques.</div>
                </button>
            
            </div>
        </div>
        
        <div class="question-container">
            <div class="question-header">
                <div class="question-number">3</div>
                <div class="question-text">Comment un autoencodeur peut-il détecter une anomalie lorsqu'il est entraîné uniquement sur des images d'un seul chiffre (par exemple le chiffre 5) dans le dataset MNIST ?  </div>
            </div>
            <div class="answers">
        
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 3)" data-question="3">
                    <div class="answer-option">A</div>
                    <div class="answer-text">Par une classification directe en sortie.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, true, 'B', 3)" data-question="3">
                    <div class="answer-option">B</div>
                    <div class="answer-text">En analysant la qualité de la reconstruction : une mauvaise reconstruction d'une image différente du chiffre entraîné indique une anomalie.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 3)" data-question="3">
                    <div class="answer-option">C</div>
                    <div class="answer-text">En calculant la distance entre l'image d'entrée et un vecteur moyen.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 3)" data-question="3">
                    <div class="answer-option">D</div>
                    <div class="answer-text">En utilisant un réseau de neurones convolutifs uniquement.</div>
                </button>
            
            </div>
        </div>
        
        <div class="question-container">
            <div class="question-header">
                <div class="question-number">4</div>
                <div class="question-text">Quelle fonction de perte est utilisée pour entraîner un autoencodeur sur des images du dataset MNIST afin de quantifier la qualité de la reconstruction ?  </div>
            </div>
            <div class="answers">
        
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 4)" data-question="4">
                    <div class="answer-option">A</div>
                    <div class="answer-text">Cross Entropy, car c'est une tâche de classification.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, true, 'B', 4)" data-question="4">
                    <div class="answer-option">B</div>
                    <div class="answer-text">MSELoss (perte quadratique moyenne), qui calcule la moyenne des carrés des différences pixel à pixel entre l'image originale et l'image reconstruite.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 4)" data-question="4">
                    <div class="answer-option">C</div>
                    <div class="answer-text">Hinge Loss, pour maximiser la marge entre classes.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 4)" data-question="4">
                    <div class="answer-option">D</div>
                    <div class="answer-text">L1 Loss, pour pénaliser les erreurs absolues.</div>
                </button>
            
            </div>
        </div>
        
        <div class="question-container">
            <div class="question-header">
                <div class="question-number">5</div>
                <div class="question-text">Quel est le rôle de la couche Sigmoid dans le décodeur de l'autoencodeur simple utilisé pour reconstruire des images en niveaux de gris normalisées entre 0 et 1, comme celles du dataset MNIST ?  </div>
            </div>
            <div class="answers">
        
                <button class="answer-button" onclick="checkAnswer(this, true, 'A', 5)" data-question="5">
                    <div class="answer-option">A</div>
                    <div class="answer-text">Normaliser les sorties pour qu'elles soient comprises entre 0 et 1, correspondant à l'intervalle des valeurs de pixels des images MNIST.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'A', 5)" data-question="5">
                    <div class="answer-option">B</div>
                    <div class="answer-text">Appliquer une activation linéaire pour accélérer l'entraînement.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'A', 5)" data-question="5">
                    <div class="answer-option">C</div>
                    <div class="answer-text">Augmenter la profondeur du réseau.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'A', 5)" data-question="5">
                    <div class="answer-option">D</div>
                    <div class="answer-text">Introduire la non-linéarité pour encoder les données.</div>
                </button>
            
            </div>
        </div>
        
        <div class="question-container">
            <div class="question-header">
                <div class="question-number">6</div>
                <div class="question-text">Dans le contexte du "denoising autoencodeur", quelle est la principale différence dans les données d'entrée et de sortie lors de l'entraînement ?  </div>
            </div>
            <div class="answers">
        
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 6)" data-question="6">
                    <div class="answer-option">A</div>
                    <div class="answer-text">L'entrée est une image nette et la sortie est une image bruitée.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, true, 'B', 6)" data-question="6">
                    <div class="answer-option">B</div>
                    <div class="answer-text">L'entrée est une image bruitée et la sortie est une image nette originale.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 6)" data-question="6">
                    <div class="answer-option">C</div>
                    <div class="answer-text">L'entrée et la sortie sont toutes deux des images bruitées mais avec différents niveaux de bruit.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 6)" data-question="6">
                    <div class="answer-option">D</div>
                    <div class="answer-text">L'entrée est une image nette et la sortie est une image reconstruite au hasard.</div>
                </button>
            
            </div>
        </div>
        
        <div class="question-container">
            <div class="question-header">
                <div class="question-number">7</div>
                <div class="question-text">Pourquoi utilise-t-on un autoencodeur convolutif dans le cas du denoising sur MNIST plutôt qu’un autoencodeur à couches entièrement connectées ?  </div>
            </div>
            <div class="answers">
        
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 7)" data-question="7">
                    <div class="answer-option">A</div>
                    <div class="answer-text">Les autoencodeurs convolutifs sont spécialement conçus pour traiter des données séquentielles.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, true, 'B', 7)" data-question="7">
                    <div class="answer-option">B</div>
                    <div class="answer-text">Les autoencodeurs convolutifs exploitent la structure spatiale des images et sont plus adaptés au traitement d'images.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 7)" data-question="7">
                    <div class="answer-option">C</div>
                    <div class="answer-text">Les autoencodeurs entièrement connectés sont trop rapides et ne convergent pas.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 7)" data-question="7">
                    <div class="answer-option">D</div>
                    <div class="answer-text">Les autoencodeurs convolutifs ont moins de paramètres que les couches entièrement connectées.</div>
                </button>
            
            </div>
        </div>
        
        <div class="question-container">
            <div class="question-header">
                <div class="question-number">8</div>
                <div class="question-text">Quel est l'impact du niveau de bruit (variance) ajouté aux images sur la tâche de denoising ?  </div>
            </div>
            <div class="answers">
        
                <button class="answer-button" onclick="checkAnswer(this, false, 'C', 8)" data-question="8">
                    <div class="answer-option">A</div>
                    <div class="answer-text">Plus le niveau de bruit est élevé, plus la tâche de débruitage devient facile.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'C', 8)" data-question="8">
                    <div class="answer-option">B</div>
                    <div class="answer-text">Le niveau de bruit n'a aucun impact sur la performance du modèle.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, true, 'C', 8)" data-question="8">
                    <div class="answer-option">C</div>
                    <div class="answer-text">Plus le niveau de bruit est élevé, plus la tâche de débruitage est difficile et les artefacts de reconstruction peuvent augmenter.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'C', 8)" data-question="8">
                    <div class="answer-option">D</div>
                    <div class="answer-text">Le modèle ignore le bruit s'il est gaussien.</div>
                </button>
            
            </div>
        </div>
        
        <div class="question-container">
            <div class="question-header">
                <div class="question-number">9</div>
                <div class="question-text">Quel rôle joue la fonction BatchNorm dans les couches de l’autoencodeur convolutif utilisé pour le denoising ?  </div>
            </div>
            <div class="answers">
        
                <button class="answer-button" onclick="checkAnswer(this, true, 'A', 9)" data-question="9">
                    <div class="answer-option">A</div>
                    <div class="answer-text">Elle normalise les activations pour stabiliser et accélérer l’apprentissage.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'A', 9)" data-question="9">
                    <div class="answer-option">B</div>
                    <div class="answer-text">Elle ajoute du bruit aux activations pour régulariser le modèle.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'A', 9)" data-question="9">
                    <div class="answer-option">C</div>
                    <div class="answer-text">Elle remplace la fonction d’activation ReLU.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'A', 9)" data-question="9">
                    <div class="answer-option">D</div>
                    <div class="answer-text">Elle réduit la taille des images en sortie.</div>
                </button>
            
            </div>
        </div>
        
        <div class="question-container">
            <div class="question-header">
                <div class="question-number">10</div>
                <div class="question-text">Quel est un avantage potentiel de tester l'architecture U-Net pour la tâche de denoising par rapport à un autoencodeur classique ?  </div>
            </div>
            <div class="answers">
        
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 10)" data-question="10">
                    <div class="answer-option">A</div>
                    <div class="answer-text">U-Net est plus simple et nécessite moins de données.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, true, 'B', 10)" data-question="10">
                    <div class="answer-option">B</div>
                    <div class="answer-text">U-Net permet de mieux préserver les détails grâce aux connexions de saut entre encodeur et décodeur.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 10)" data-question="10">
                    <div class="answer-option">C</div>
                    <div class="answer-text">U-Net ne peut pas être utilisé pour la reconstruction d'images.</div>
                </button>
            
                <button class="answer-button" onclick="checkAnswer(this, false, 'B', 10)" data-question="10">
                    <div class="answer-option">D</div>
                    <div class="answer-text">U-Net est uniquement adapté aux images en couleur.</div>
                </button>
            
            </div>
        </div>
        
    <div class="score-container">
        <div class="score-text" id="scoreDisplay">Score: 0/10</div>
    </div>
</div>

<script>
    let totalQuestions = 10;
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
    
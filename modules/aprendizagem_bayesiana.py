import weka.core.jvm as jvm

from weka.classifiers import Classifier
from weka.core.converters import load_any_file
from weka.core.dataset import Attribute, Instance, Instances
from weka.classifiers import Classifier, Evaluation
jvm.start()

class AprendizagemBayesiana:

    def __init__(self):
        pass

    @staticmethod
    def bayes_classifier(features):
        #carrega o dataset
        instancias = load_any_file("caracteristicas.arff")
        # sinaliza que o ultimo atributo é a classe
        instancias.class_is_last()
        # Carrega o classificafor Naive Bayes e Classifica com base nas características da imagem
        classifier = Classifier(classname="weka.classifiers.bayes.NaiveBayes")
        classifier.build_classifier(instancias)
        # Cria uma nova instância com base nas caracteristicas extraidas
        new_instance = Instance.create_instance(features)
        # Adiciona a nova instância ao dataset
        instancias.add_instance(new_instance)
        # Liga a nova instancia ao dataset
        new_instance.dataset = instancias
        # Classifica a nova instância trazendo as probabilidades de ela pertencer as classes definidas
        classification = classifier.distribution_for_instance(new_instance)

        print("Classificação", " - Apu: ", round(classification[0]*100,2), "  Nelson: ", round(classification[1],2))

        return classification




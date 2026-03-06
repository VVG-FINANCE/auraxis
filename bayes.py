# =========================
# bayes.py - Auraxis robusto
# =========================
import numpy as np

class Bayes:
    """
    Ajuste de probabilidades de score e tendência usando Estatística Bayesiana
    """

    def __init__(self):
        self.prior_score = 0.5  # probabilidade inicial
        self.historico = []

    def atualizar_historico(self, evento_sucesso):
        """
        Adiciona observação ao histórico
        :param evento_sucesso: True/False indicando acerto
        """
        self.historico.append(evento_sucesso)

    def probabilidade_posterior(self):
        """
        Calcula probabilidade posterior P(H|E) usando Bayes simples
        """
        if not self.historico:
            return self.prior_score

        n_sucesso = sum(self.historico)
        n_total = len(self.historico)
        # Posterior = P(H|E) = (sucessos + 1)/(total + 2) -> Laplace smoothing
        posterior = (n_sucesso + 1) / (n_total + 2)
        return round(posterior, 4)

    def ajustar_score(self, score_base):
        """
        Ajusta score com probabilidade Bayesiana
        """
        posterior = self.probabilidade_posterior()
        score_ajustado = round(score_base * posterior, 2)
        return score_ajustado

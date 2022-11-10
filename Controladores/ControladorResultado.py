from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioResultado.findAll()
    """
    Asignacion estudiante y materia a inscripción(este es de guia)
    Asignacion mesa y candidato a Resultados
    """
    def create(self,infoResultado,numero_mesa,cedula_candidato):
        nuevoResultado=Resultado(infoResultado)
        laMesa=Mesa(self.repositorioMesa.findById(numero_mesa))
        elCandidato=Candidato(self.repositorioCandidato.findById(cedula_candidato))
        nuevoResultado.numero_mesa=laMesa
        nuevoResultado.candidato=elCandidato
        return self.repositorioResultado.save(nuevoResultado)
    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    """
    Modificación de inscripción (estudiante y materia) (ejemplo)
    Modificación de Resultado (mesa y candidato)
    """
    def update(self,id,infoResultado,numero_mesa,cedula_candidato):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        elResultado.votos=infoResultado["votos"]
        laMesa = Mesa(self.repositorioMesa.findById(numero_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(cedula_candidato))
        elResultado.numero_mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultado.save(elResultado)
    def delete(self, id):
        return self.repositorioResultado.delete(id)
    "Obtener todos los inscritos en un candidato"
    def listarInscritosEnCandidato(self,id_candidato):
        return self.repositorioResultado.getListadoInscritosEnCandidato(id_candidato)
    def listarInscritosEnMesa(self,id_mesa):
        return self.repositorioResultado.getListadoInscritosEnMesa(id_mesa)
    def votosMasAltosPorMesa(self):
        return self.repositorioResultado.getMayorVotosCandidato()
    def delete(self, id):
        return self.repositorioResultado.delete(id)
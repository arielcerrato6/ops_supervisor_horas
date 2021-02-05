import logging
import math

from collections import namedtuple

from datetime import datetime, time
from pytz import timezone, UTC

from odoo import api, fields, models
from odoo.addons.resource.models.resource import float_to_time, HOURS_PER_DAY
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools import float_compare
from odoo.tools.float_utils import float_round
from odoo.tools.translate import _

_logger = logging.getLogger(__name__)

tipo_camisas = [
    ('xs', 'xs'),
    ('s', 's'),
    ('m', 'm'),
    ('l', 'l'),
    ('xl', 'xl'),
    ('xxl', 'xxl'),
]

personas_depen = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
]

seleccion_si = [
    ('SI', 'Si'),
    ('NO', 'No'),
]


class Ops_Inherints_empleados(models.Model):
    _inherit = "hr.employee"

    
    dimension = fields.Char("Dimension")
    tipo_camisa = fields.Selection(tipo_camisas, string='Camisa', index=True, default=tipo_camisas[0][0])
    rtn_emple = fields.Char("RTN")
    correo_personals = fields.Char("Correo Personal")
    cuenta_bancaria_personal = fields.Char("# Cuenta Bancaria")
    


    descri_ingreso = fields.Char("Descripción de ingresos")
    personas_dependen = fields.Selection(personas_depen, string='¿Cuántas personas dependen económicamente de usted?', index=True, default=personas_depen[0][0])
   
   
    vive_en_casa = fields.Selection(seleccion_si, string='Vive en casa propia', index=True, default=seleccion_si[0][0])
    paga_renta = fields.Boolean('Paga Renta', default=False)
    renta_mensual = fields.Char("Renta Mensual")
    pariente_trabaja = fields.Boolean('¿Algun pariente trabaja en esta empresa?', default=False)
    periente_ops = fields.Char("Nombre del pariente que labora en OPS")
    auto_propio = fields.Boolean('Posee automóvil propio', default=False)


    tiene_otro_ingreso = fields.Selection(seleccion_si, string='Tiene otro ingreso', index=True, default=seleccion_si[0][0])
    

    tiene_deudas = fields.Boolean('Tiene deudas', default=False)

    domicilio_he = fields.Char("Domicilio")
    fecha_ingreso = fields.Date("Fecha Ingreso")
    profesion_hn = fields.Char("Profesion")
    no_cartera = fields.Boolean('No pertenece a campañas', default=False)



    _sql_constraints = [
        ('name_uniq', 'unique (identification_id)', "El numero de identidad ya existe !"),
    ]
    
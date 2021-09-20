from flask import Blueprint, request, jsonify
from modules.networking import conversion_methods
from modules.auth_methods import Restricted

networking = Blueprint('networking', __name__)
convert = conversion_methods()

@networking.route("/cidr-to-mask")
@Restricted.requiere_token
def urlCidrToMask():
     """
     url example:
          e.g. http://127.0.0.1:8000/cidr-to-mask?value=8
     Gets CIDR value from GET request and returns a json response
     with the form:
          { "function": "cidrToMask" 
               "input": <value-from-request>
               "output": <calculated-mask>
          }
     Requieres authentication token
     """
     cidr = request.args.get('value')
     json_response = jsonify({ 
          "function": "cidrToMask",
          "input": cidr,
          "output": convert.cidr_to_mask(cidr) 
     })
     return json_response


@networking.route("/mask-to-cidr")
@Restricted.requiere_token
def urlMaskToCidr():
     """
     url example:
          e.g. http://127.0.0.1:8000/mask-to-cidr?value=255.0.0.0
     Gets mask value from GET request and returns a json response
     with the form:
          { "function": "cidrToMask" 
               "input": <value-from-request>
               "output": <calculated-CIDR>
          }
     Requieres authentication token
     """
     mask = request.args.get('value')
     json_response = jsonify({
          "function": "maskToCidr",
          "input": mask,
          "output": convert.mask_to_cidr(mask)
     })
     return json_response

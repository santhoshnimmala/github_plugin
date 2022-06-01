#Murex Copyright disclaimer
#Copyright Murex S.A.S., 2003-2019. All Rights Reserved.
#
#This software program is proprietary and confidential to Murex S.A.S and its
#affiliates ("Murex") and, without limiting the generality of the foregoing
#reservation of rights, shall not be accessed, used, reproduced or distributed
#without the express prior written consent of Murex and subject to the
#applicable Murex licensing terms.
#
#Any modification or removal of this copyright notice is expressly prohibited.
#Murex Copyright disclaimer
# Description:
# This script is called by the MXpipeline seed.py file that is under mxpipeline/core/config
# A variable file is passed as a parameter to this script via the --var-file argument so that you can parameterize you git server configuration

import argparse

parser = argparse.ArgumentParser(description='Install MXpipeline')
parser.add_argument('--var-file', dest='var_file', type=argparse.FileType('r'),
                    required=True, help="variable file for MXpipeline seed")

args = parser.parse_args()
var_file_path = args.var_file.name

# TODO: 
# Call the git server api(s) to create the needed webhooks, etc... 
# raise NotImplementedError
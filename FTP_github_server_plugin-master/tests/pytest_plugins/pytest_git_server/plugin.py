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
import pytest
from tests.system.models.servers import IGitServer
from tests.system.models.infra import IGitServerInfraProvider

@pytest.fixture
def git_server(git_server_infra):
    # type: (IGitServerInfraProvider) -> IGitServer
    raise NotImplementedError

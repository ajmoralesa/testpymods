def dame_arch_data(archpaths):
    """""This function gathers architecture data from .txt files

    Arguments:
        archpaths {list} -- list of paths to every folder containing architecture data

    Returns:
        [dict] -- Returns dictionary containing all data for each path
    """

    import os
    import fnmatch

    archdata = dict()
    for participant in archpaths.keys():

        sessions = dict()
        for ntest in archpaths[participant].keys():
            print('Este es el test de: ', participant, 'sesion: ', ntest)
            path = archpaths[participant][ntest]

            # '_bfs.txt' and '_sms.txt' refer to single image files only
            files = os.listdir(path)

            bf_files = {'simple': fnmatch.filter(files, str('*_bfs.txt')),
                        'panoramic': fnmatch.filter(files, str('*_bfp.txt')),
                        'landmark': fnmatch.filter(files, str('*_bfpm.txt'))}

            sm_files = {'simple': fnmatch.filter(files, str('*_sms.txt')),
                        'panoramic': fnmatch.filter(files, str('*_smp.txt')),
                        'landmark': fnmatch.filter(files, str('*_smpm.txt'))}

            # get data
            bf_data = _organize_arch(fils=bf_files, pth=path)
            sm_data = _organize_arch(fils=sm_files, pth=path)

            muscles = dict()
            muscles['BF'] = bf_data
            muscles['SM'] = sm_data

            sessions[ntest] = muscles

        archdata[participant] = sessions

    return _calcula_arch(data=archdata)

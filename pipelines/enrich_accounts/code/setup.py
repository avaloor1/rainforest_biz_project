from setuptools import setup, find_packages
setup(
    name = 'enrich_accounts',
    version = '1.0',
    packages = find_packages(include = ('enrich_accounts*', )) + ['prophecy_config_instances.enrich_accounts'],
    package_dir = {'prophecy_config_instances.enrich_accounts' : 'configs/resources/enrich_accounts'},
    package_data = {'prophecy_config_instances.enrich_accounts' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.49'],
    entry_points = {
'console_scripts' : [
'main = enrich_accounts.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)

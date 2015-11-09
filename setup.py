from setuptools import setup

setup(
        name="pythonrouge",
        version="0.0.1",
        description="ROUGE script using python",
        url="http://github.com/tagucci/pythonrouge",
        author="tagucci",
        author_email="taguchi.yuya.to0@is.naist.jp",
        keywords=["NL", "CL", "natural language processing", "computational linguistics", "summrization"],
        packages=["pythonrouge"],
        package_data={
            'pythonrouge': ['ROUGE-1.5.5/*.*',
                  'ROUGE-1.5.5/XML/*.*',
                  'ROUGE-1.5.5/XML/DOM/*.*',
                  'ROUGE-1.5.5/XML/Handler/*.*',
                  'ROUGE-1.5.5/data/WordNet-2.0.exc.db',
                  'ROUGE-1.5.5/data/smart_common_words.txt',
                  'ROUGE-1.5.5/data/WordNet-1.6-Exceptions/*.*',
                  'ROUGE-1.5.5/data/WordNet-2.0-Exceptions/*.*',
                  ],
       },
       )

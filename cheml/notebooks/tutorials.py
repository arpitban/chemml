def tutorial1():
    script = """## (Enter,table)
    << host = pandas
    << function = read_table
    << sep = ,
    << filepath_or_buffer = benchmarks/sample_data/RI/RI_data.csv
    >> df 0

## (Prepare,basic operators)
    << host = cheml
    << function = Split
    << selection = ['Mol_Smiles']
    >> 0 df
    >> df1 1
    >> df2 5

## (Store,file)
    << host = cheml
    << function = SaveFile
    << format = smi
    << header = False
    << filename = smi
    >> 1 df
    >> filepath 2
    >> filepath 4

## (Prepare,feature representation)
    << host = cheml
    << function = Dragon
    << molFile = @molfile
    >> 2 molfile
    >> df 3

## (Store,file)
    << host = cheml
    << function = SaveFile
    << filename = dragon
    >> 3 df

## (Prepare,feature representation)
    << host = cheml
    << function = RDKitFingerprint
    << molfile = @molfile
    >> 4 molfile
    >> df 7

## (Prepare,basic operators)
    << host = cheml
    << function = Split
    << selection = ['RI_LL']
    >> 5 df
    >> df1 6

## (Model,regression)
    << host = sklearn
    << function = MLPRegressor
    << func_method = fit
    >> 6 dfy
    >> 7 dfx
    >> dfy_predict 8

## (Enter,python script)
    << host = cheml
    << function = PyScript
    << line01 = print iv1.describe()
    >> 8 iv1

            """
    return script.strip().split('\n')

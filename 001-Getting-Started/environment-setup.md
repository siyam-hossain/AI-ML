## **Data Science environment setup [bash]**

#### **Initialize conda first**
```bash
conda init
```

#### **Create env**
```bash
conda create --prefix ./env
```

#### **Activate env**
```bash
conda activate ./env
```

#### **⭐Optional: creating requirements.txt**
```bash
conda list -e > requirements.txt
```

#### **⭐Optional: how to use requirements.txt**
```bash
conda create --prefix ./env --file requirements.txt
```

#### **Install jupyter**
```bash
conda install jupyter
```

#### **Install tools & libraries**
```bash
conda install pandas numpy matplotlib scikit-learn
```

#### **Run jupyter notebook**
```bash
jupyter notebook
```

#### **If you want to deactivate env**
```bash
conda deactivate
```

<table>
  <tr>
    <th colspan="2">Jupyter notebook shortcut</th>
  </tr>
  <tr>
    <td>markdown</td>
    <td><code>string</code></td>
  </tr>
  <tr>
    <td>code</td>
    <td><code>y</code></td>
  </tr>
  <tr>
    <td>run only a cell</td>
    <td><code>Ctrl + Enter</code></td>
  </tr>
  <tr>
    <td>run only a cell and create a new cell</td>
    <td><code>Shift + Enter</code></td>
  </tr>
  <tr>
    <td>add a cell above</td>
    <td><code>A</code></td>
  </tr>
  <tr>
    <td>add a cell below</td>
    <td><code>B</code></td>
  </tr>
  <tr>
    <td>delete current cell</td>
    <td><code>DD</code></td>
  </tr>
  <tr>
    <td>terminal command</td>
    <td><code>ls</code></td>
  </tr>
</table>

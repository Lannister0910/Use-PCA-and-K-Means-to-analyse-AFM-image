import numpy as np;



class PCA:
    def __init__(self, rate=0.85, is_normal=False):
        self.rate = rate;
        self.is_normal = is_normal;

    def average(self, x, ready=False):
        aver = sum(x) / len(x);
        x_1 = x if ready else np.array(x).T;
        x_aver = [aver(a) for a in x_1];
        x_aver = np.array(x_aver);
        # 相当于x_aver = np.mean(x_1,axis=1);
        return x_aver;

    def std(self, x, ready=False):
        x_1 = x if ready else np.array(x).T;
        s = [];
        for a in x_1:
            s.append(np.std(a));
        s = np.array(s);
        return s;

    def cov(self, x, ready=False):
        x_1 = x if ready else np.array(x).T;
        return np.cov(x_1);

    def eigen(self, cov_mat):
        '''vals: 特征值，list类型
        vecs：特征向量，按行摆放，一行即一个向量,ndarray类型'''
        vals, vecs = np.linalg.eig(cov_mat);  # 输出类型为ndarray类型
        vecs = vecs.T;
        vals_new = sorted(vals, reverse=True);  # 按从大到小排列
        vecs_new = np.array([vecs[vals.tolist().index(a)] for a in vals_new]);
        return vals_new, vecs_new;

    def contribution(self, vals):
        sum_val = sum(vals);
        ctr = [a / sum_val for a in vals];
        return ctr;

    def pca_k(self, ctr, rate):
        sum_ctr = 0;
        for i in range(len(ctr)):
            sum_ctr += ctr[i];
            if sum_ctr >= rate:
                return i + 1;

    def normalization(self, X, ready=False):
        X = X if ready else np.array(X);
        X_new = (X - self.aver) / self.s;
        return X_new;

    def fit(self, X):
        x = np.array(X).T;
        if self.is_normal:
            self.aver = self.average(x, True);  # 求平均
            self.s = self.std(x, True);  # 求标准差
            x = self.normalization(x.T, True).T;  # 进行标准化处理
        self.cov_mat = self.cov(x, True);  # 求协方差矩阵
        self.vals, self.vecs = self.eigen(self.cov_mat);  # 求特征值和特征向量
        self.ctr = self.contribution(self.vals);  # 求主成分的方差贡献率
        self.k = self.pca_k(self.ctr, self.rate);  # 或取主成分的k值
        self.covv = self.vecs[:self.k];  # 组成关系矩阵
        if self.is_normal:
            lmk = np.sqrt(np.array(self.vals)).T;
            self.covv = self.covv * lmk;

    def transfer(self, X):
        x_1 = np.array(X);
        if self.is_normal:
            x_1 = self.normalization(x_1, True);
        y = [];
        for x in x_1:
            y.append(np.matmul(self.covv, x).T);
        y = np.array(y).tolist();
        return y;

x1 = [149.5, 162.5, 162.7, 162.2, 156.5, 156.1, 172.0, 173.2, 159.5, 157.7];
x2 = [69.5, 77.0, 78.5, 87.5, 74.5, 74.5, 76.5, 81.5, 74.5, 79.0];
x3 = [38.5, 55.5, 50.8, 65.5, 49.0, 45.5, 51.0, 59.5, 43.5, 53.5];
x = [[a, x2[x1.index(a)], x3[x1.index(a)]] for a in x1];

pca = PCA(rate=0.9, is_normal=False);
pca.fit(x);

print('协方差矩阵为：', pca.cov_mat, '-------------------------', sep='\n');
print('特征值为λ：', pca.vals, '-------------------------', '特征向量矩阵为：', pca.vecs, '-------------------------', sep='\n');
print('主成分的k值', pca.k, '-------------------------', '按照主成分的值选取特征向量矩阵',pca.covv, '-------------------------', sep='\n');
print('主成基变换之后的Y（Y=PX）', np.array(pca.transfer(x[:10])));

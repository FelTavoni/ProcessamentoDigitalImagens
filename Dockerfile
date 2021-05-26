FROM jupyter/datascience-notebook

RUN conda install --yes scikit-learn scipy numpy matplotlib && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER
ENV JUPYTER_ENABLE_LAB=yes

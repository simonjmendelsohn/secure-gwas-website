import os
from copy import deepcopy
from typing import Any, Dict, List, Union

FLASK_DEBUG = os.getenv("FLASK_DEBUG")
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")

TERRA = os.getenv("TERRA", "")
TERRA_CP0_CONFIG_NAMESPACE = os.getenv("TERRA_CP0_CONFIG_NAMESPACE", "")
TERRA_CP0_CONFIG_NAME = os.getenv("TERRA_CP0_CONFIG_NAME", "")
TERRA_CP0_WORKSPACE_NAMESPACE = os.getenv("TERRA_CP0_WORKSPACE_NAMESPACE", "")
TERRA_CP0_WORKSPACE_NAME = os.getenv("TERRA_CP0_WORKSPACE_NAME", "")

RAWLS_API_URL = os.getenv("RAWLS_API_URL", "https://rawls.dsde-dev.broadinstitute.org")
SAM_API_URL = os.getenv("SAM_API_URL", "https://sam.dsde-dev.broadinstitute.org")
SFKIT_API_URL = os.getenv("SFKIT_API_URL", "http://localhost:8080")
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")
APP_VERSION = os.getenv("APP_VERSION", "")
BUILD_VERSION = os.getenv("BUILD_VERSION", "")
CLOUD_RUN = os.getenv("CLOUD_RUN", "False")
RESULTS_BUCKET = os.getenv("RESULTS_BUCKET", "sfkit")
SERVICE_URL = os.getenv("SERVICE_URL", "")
SERVER_GCP_PROJECT = "broad-cho-priv1"
SERVER_REGION = "us-central1"
SERVER_ZONE = f"{SERVER_REGION}-a"
NETWORK_NAME_ROOT = "sfkit"
INSTANCE_NAME_ROOT = "sfkit"
DEVELOPER_USER_ID = "developer"
GOOGLE_CLIENT_ID = (
    "419003787216-rcif34r976a9qm3818qgeqed7c582od6.apps.googleusercontent.com"
)
# these are used only when TERRA is NOT set
AZURE_B2C_CLIENT_ID = os.getenv(
    "AZURE_B2C_CLIENT_ID", "a605ffae-592a-4096-b029-78ba66b6d614"
)  # public; used for authentication
AZURE_B2C_JWKS_URL = os.getenv(
    "AZURE_B2C_JWKS_URL",
    "https://sfkitdevb2c.b2clogin.com/sfkitdevb2c.onmicrosoft.com/discovery/v2.0/keys?p=B2C_1_signupsignin1",
)

FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")
FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID", SERVER_GCP_PROJECT)
FIRESTORE_DATABASE = os.getenv("FIRESTORE_DATABASE", "(default)")

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "")
SENDGRID_FROM_EMAIL = os.getenv("SENDGRID_FROM_EMAIL", "")

SENTRY_DSN = os.getenv("SENTRY_DSN", "")
SENTRY_ENVIRONMENT = os.getenv("SENTRY_ENVIRONMENT", "development")

PARAMETERS_TYPE = Dict[str, Union[Dict[str, Any], List[str]]]

MPCGWAS_SHARED_PARAMETERS = {
    "NUM_SNPS": {
        "name": "Number of Single Nucleotide Polymorphisms",
        "description": "The number of SNPs (Single Nucleotide Polymorphisms) in the dataset.",
        "value": 28021,
    },
    "NUM_COVS": {
        "name": "Number of Covariates",
        "description": "The number of covariate features in the dataset.",
        "value": 3,
    },
    "NUM_DIM_TO_REMOVE": {
        "name": "Number of PCs for Population Stratification",
        "description": "The number of principal components to correct for (in the PCA).",
        "value": 5,
    },
    "SKIP_QC": {
        "name": "Skip Quality Control",
        "description": "A binary value to skip quality control and use all individuals/SNPs.",
        "value": 0,
    },
    "IMISS_UB": {
        "name": "Individual Missing Rate Upper Bound",
        "description": "The individual missing rate upper bound.",
        "value": 1.0,
    },
    "HET_LB": {
        "name": "Heterozygosity Lower Bound",
        "description": "The individual heterozygosity lower bound.",
        "value": 0.0,
    },
    "HET_UB": {
        "name": "Heterozygosity Upper Bound",
        "description": "The individual heterozygosity upper bound.",
        "value": 0.5,
    },
    "GMISS_UB": {
        "name": "Genotype Missing Rate Upper Bound",
        "description": "The genotype missing rate upper bound.",
        "value": 0.1,
    },
    "MAF_LB": {
        "name": "Minor Allele Frequency Lower Bound",
        "description": "The minor allele frequency lower bound.",
        "value": 0.01,
    },
    "MAF_UB": {
        "name": "Minor Allele Frequency Upper Bound",
        "description": "The minor allele frequency upper bound.",
        "value": 0.99,
    },
    "HWE_UB": {
        "name": "Hardy Weinberg Equilibrium Upper Bound",
        "description": "The hardy weinberg equilibrium test statistic upper bound.",
        "value": 28.374,
    },
    "LD_DIST_THRES": {
        "name": "LD Distance Threshold",
        "description": "The genomic distance threshold for selecting SNPs for principal component analysis.",
        "value": 100000,
    },
    "index": [  # index is used to order the parameters in the UI
        "NUM_SNPS",
        "NUM_COVS",
        "NUM_DIM_TO_REMOVE",
        "SKIP_QC",
        "IMISS_UB",
        "HET_LB",
        "HET_UB",
        "GMISS_UB",
        "MAF_LB",
        "MAF_UB",
        "HWE_UB",
        "LD_DIST_THRES",
    ],
}

MPCGWAS_ADVANCED_PARAMETERS = {
    "ITER_PER_EVAL": {
        "name": "Iterations per Evaluation",
        "description": "The number of QR iterations per eigenvalue when performing eigendecomposition.",
        "value": 5,
    },
    "NUM_OVERSAMPLE": {
        "name": "Oversampling Parameter for PCA",
        "description": "An oversampling parameter for randomized principal component analysis: \
            how many extra components should be extracted to improve the accuracy.",
        "value": 10,
    },
    "NUM_POWER_ITER": {
        "name": "Number of Power Iterations",
        "description": "The number of power iterations during the randomized PCA.",
        "value": 20,
    },
    "NBIT_K": {
        "name": "NBIT_K",
        "description": "Total number of bits used to represent data values",
        "value": 90,
    },
    "NBIT_F": {
        "name": "NBIT_F",
        "description": "Number of bits assigned to the fractional range",
        "value": 30,
    },
    "NBIT_V": {
        "name": "NBIT_V",
        "description": "Number of additional bits used as a buffer for statistical security",
        "value": 64,
    },
    "BASE_P": {
        "name": "BASE_P",
        "description": "Base prime used for cryptography (default is the largest 160 bit prime)",
        "value": "1461501637330902918203684832716283019655932542929",
    },
    "index": [  # index is used to order the parameters in the UI
        "ITER_PER_EVAL",
        "NUM_OVERSAMPLE",
        "NUM_POWER_ITER",
        "NBIT_K",
        "NBIT_F",
        "NBIT_V",
        "BASE_P",
    ],
}

PCA_SHARED_PARAMETERS = {
    "num_columns": {
        "name": "Number of Columns",
        "description": "The number of columns in the dataset.",
        "value": 28021,
    },
    "num_pcs_to_remove": {
        "name": "Number of Principal Components",
        "description": "The number of principal components to extract.",
        "value": 5,
    },
    "index": [  # index is used to order the parameters in the UI
        "num_columns",
        "num_pcs_to_remove",
    ],
}

PCA_ADVANCED_PARAMETERS = {
    "iter_per_eigenval": {
        "name": "Iterations per Evaluation",
        "description": "The number of QR iterations per eigenvalue when performing eigendecomposition.",
        "value": 5,
    },
    "num_oversampling": {
        "name": "Oversampling Parameter for PCA",
        "description": "An oversampling parameter for randomized principal component analysis: \
            how many extra components should be extracted to improve the accuracy.",
        "value": 10,
    },
    "num_power_iters": {
        "name": "Number of Power Iterations",
        "description": "The number of power iterations during the randomized PCA.",
        "value": 2,
    },
    "mpc_field_size": {
        "name": "MPC Field Size",
        "description": "MPC Field Size",
        "value": 256,
    },
    "mpc_data_bits": {
        "name": "MPC Data Bits",
        "description": "Total number of bits used to represent data values",
        "value": 90,
    },
    "mpc_frac_bits": {
        "name": "MPC Frac Bits",
        "description": "Number of bits assigned to the fractional range",
        "value": 30,
    },
    "index": [  # index is used to order the parameters in the UI
        "iter_per_eigenval",
        "num_oversampling",
        "num_power_iters",
        "mpc_field_size",
        "mpc_data_bits",
        "mpc_frac_bits",
    ],
}

SECURE_DTI_SHARED_PARAMETERS = {
    "FEATURE_RANK": {
        "name": "Feature Rank",
        "description": "",
        "value": 6903,
    },
    "index": [
        "FEATURE_RANK",
    ],
}

SECURE_DTI_ADVANCED_PARAMETERS = {
    "NBIT_K": {
        "name": "NBIT_K",
        "description": "Total number of bits used to represent data values",
        "value": 90,
    },
    "NBIT_F": {
        "name": "NBIT_F",
        "description": "Number of bits assigned to the fractional range",
        "value": 30,
    },
    "NBIT_V": {
        "name": "NBIT_V",
        "description": "Number of additional bits used as a buffer for statistical security",
        "value": 64,
    },
    "BASE_P": {
        "name": "BASE_P",
        "description": "Base prime used for cryptography (default is the largest 160 bit prime)",
        "value": "1461501637330902918203684832716283019655932542929",
    },
    "index": [],
}

SFGWAS_SHARED_PARAMETERS = {
    "num_snps": {
        "name": "Number of Single Nucleotide Polymorphisms",
        "description": "The number of SNPs in the dataset.",
        "value": 28021,
    },
    "num_covs": {
        "name": "Number of Covariates",
        "description": "The number of covariates in the dataset.",
        "value": 2,
    },
    "num_pcs_to_remove": {
        "name": "Number of PCs for Population Stratification",
        "description": "The number of principal components to correct for (in the PCA).",
        "value": 5,
    },
    "skip_qc": {
        "name": "Skip Quality Control",
        "description": "A binary value to skip quality control and use all individuals/SNPs.",
        "value": "false",
    },
    "imiss_ub": {
        "name": "Individual Missing Rate Upper Bound",
        "description": "The individual missing rate upper bound.",
        "value": 1.0,
    },
    "het_lb": {
        "name": "Heterozygosity Lower Bound",
        "description": "The individual heterozygosity lower bound.",
        "value": 0.0,
    },
    "het_ub": {
        "name": "Heterozygosity Upper Bound",
        "description": "The individual heterozygosity upper bound.",
        "value": 0.1,
    },
    "gmiss": {
        "name": "Genotype Missing Rate Upper Bound",
        "description": "The genotype missing rate upper bound.",
        "value": 0.1,
    },
    "maf_lb": {
        "name": "Minor Allele Frequency Lower Bound",
        "description": "The minor allele frequency lower bound.",
        "value": 0.01,
    },
    "hwe_ub": {
        "name": "Hardy Weinberg Equilibrium Upper Bound",
        "description": "The hardy weinberg equilibrium test statistic upper bound.",
        "value": 28.374,
    },
    "snp_dist_thres": {
        "name": "LD Distance Threshold",
        "description": "The genomic distance threshold for selecting SNPs for principal component analysis.",
        "value": 100000,
    },
    "index": [  # index is used to order the parameters in the UI
        "num_snps",
        "num_covs",
        "num_pcs_to_remove",
        "skip_qc",
        "imiss_ub",
        "het_lb",
        "het_ub",
        "gmiss",
        "maf_lb",
        "hwe_ub",
        "snp_dist_thres",
    ],
}

SFGWAS_ADVANCED_PARAMETERS = {
    "iter_per_eigenval": {
        "name": "Iterations per Evaluation",
        "description": "The number of QR iterations per eigenvalue when performing eigendecomposition.",
        "value": 5,
    },
    "num_oversampling": {
        "name": "Oversampling Parameter for PCA",
        "description": "An oversampling parameter for randomized principal component analysis: \
            how many extra components should be extracted to improve the accuracy.",
        "value": 10,
    },
    "num_power_iters": {
        "name": "Number of Power Iterations",
        "description": "The number of power iterations during the randomized PCA.",
        "value": 20,
    },
    "mpc_field_size": {
        "name": "MPC Field Size",
        "description": "MPC Field Size",
        "value": 256,
    },
    "mpc_data_bits": {
        "name": "MPC Data Bits",
        "description": "Total number of bits used to represent data values",
        "value": 90,
    },
    "mpc_frac_bits": {
        "name": "MPC Frac Bits",
        "description": "Number of bits assigned to the fractional range",
        "value": 30,
    },
    "index": [  # index is used to order the parameters in the UI
        "iter_per_eigenval",
        "num_oversampling",
        "num_power_iters",
        "mpc_field_size",
        "mpc_data_bits",
        "mpc_frac_bits",
    ],
}

SFRELATE_SHARED_PARAMETERS: PARAMETERS_TYPE = {"index": []}

SFRELATE_ADVANCED_PARAMETERS = {
    "PARA": {
        "name": "PARA",
        "description": "Number of parallel processes to use. Should be set as large as possible to utilize all CPUs and memory. Exact value depends on the machine and dataset sizes. Users can provide reasonable parameters like 5 and retry with a smaller one if it fails due to memory constraints.",
        "value": 2,
    },
    "ENCLEN": {
        "name": "ENCLEN",
        "description": "the number of snps in each encoded split haplotype ssegemnt (default: 80)",
        "value": 80,
    },
    "SEGLEN": {
        "name": "SEGLEN",
        "description": "centi-Morgan length of each split haplotype segment (default: 8.0)",
        "value": 8.0,
    },
    "STEPLEN": {
        "name": "STEPLEN",
        "description": "centi-Morgan spacing between the beginning of each split haplotype segment (default: 4.0)",
        "value": 4.0,
    },
    "K": {
        "name": "K",
        "description": "number of SNPs in each kSNP token for hashing (default: 8)",
        "value": 8,
    },
    "L": {
        "name": "L",
        "description": "number of hash tokens to construct every hash index (default: 4)",
        "value": 4,
    },
    "MAXL": {
        "name": "MAXL",
        "description": "max number of repetitive hashing; increase and retry if table saturation is low (default: 6)",
        "value": 6,
    },
    "s": {
        "name": "s",
        "description": "subsampling rate (default: 0.7)",
        "value": 0.7,
    },
    "index": [
        "PARA",
        "ENCLEN",
        "SEGLEN",
        "STEPLEN",
        "K",
        "L",
        "MAXL",
        "s",
    ],
}


SHARED_PARAMETERS = {
    "MPC-GWAS": MPCGWAS_SHARED_PARAMETERS,
    "PCA": PCA_SHARED_PARAMETERS,
    "Secure-DTI": SECURE_DTI_SHARED_PARAMETERS,
    "SF-GWAS": SFGWAS_SHARED_PARAMETERS,
    "SF-RELATE": SFRELATE_SHARED_PARAMETERS,
}

ADVANCED_PARAMETERS = {
    "MPC-GWAS": MPCGWAS_ADVANCED_PARAMETERS,
    "PCA": PCA_ADVANCED_PARAMETERS,
    "Secure-DTI": SECURE_DTI_ADVANCED_PARAMETERS,
    "SF-GWAS": SFGWAS_ADVANCED_PARAMETERS,
    "SF-RELATE": SFRELATE_ADVANCED_PARAMETERS,
}


DEFAULT_USER_PARAMETERS = {
    "PUBLIC_KEY": {
        "name": "Public Key",
        "description": "Your public cryptographic key that you and the other participant will use to \
            encrypt each of your data (combined with your respective private keys, of course).",
        "value": "",
    },
    "GCP_PROJECT": {
        "name": "GCP Project ID",
        "description": "The Project ID for the GCP project you're using (the one where you put your encrypted data \
            and the VM instance will run). If you don't have a dedicated GCP project for this workflow, \
                you will need to make one.  Note that this Project ID MAY or MAY NOT be the same as your Project Name.",
        "value": "",
    },
    "DATA_PATH": {
        "name": "GCP Path to Data",
        "description": "The path to your data in the GCP bucket.  For example, if I put the 'for_gwas' folder \
            in a bucket called 'secure-gwas-data', the path would be 'secure-gwas-data/for_gwas'.",
        "value": "",
    },
    "GENO_BINARY_FILE_PREFIX": {
        "name": "Genotype Binary File Prefix",
        "description": "Path to the genotype binary file prefix (e.g. 'geno/ch%d'). \
            This path helps sfkit locate your genotype data.",
        "value": "",
    },
    "NUM_INDS": {
        "name": "Number of Individuals",
        "description": "The number of individuals in your dataset.",
        "value": "",
    },
    "NUM_THREADS": {
        "name": "Number of Threads",
        "description": "The number of threads to use when running the GWAS",
        "value": 20,
    },
    "NUM_CPUS": {
        "name": "Number of CPUs",
        "description": "The number of CPUs to allocate to the VM instance that \
            will be running the protocol in your GCP account.",
        "value": 16,
    },
    "ZONE": {
        "name": "Zone",
        "description": "The zone where you want to run your VM instance.",
        "value": "us-central1-a",
    },
    "BOOT_DISK_SIZE": {
        "name": "Boot Disk Size",
        "description": "The size of the boot disk for your VM instance. Must be at least 10 (GB).",
        "value": 128,
    },
    "DATA_HASH": {
        "name": "Data Hash",
        "description": "The hash of the data you are using.  \
            This is used to ensure that you are using the same data that you uploaded.",
        "value": "",
    },
    "IP_ADDRESS": {
        "name": "IP Address",
        "description": "The IP address of the VM instance that will be running the GWAS protocol.",
        "value": "",
    },
    "PORTS": {
        "name": "Ports",
        "description": "The ports (comma separated) used by the VM instance that will be running the GWAS protocol.",
        "value": "null,3110,7320",
    },
    "AUTH_KEY": {
        "name": "Authentication Key",
        "description": "A key that will be used to authenticate the VM instance that will be running the protocol.",
        "value": "",
    },
    "SEND_RESULTS": {
        "name": "Visualize Results",
        "description": "Whether to send the results of the protocol to the website to be downloaded and visualized.",
        "value": "Yes",
    },
    "RESULTS_PATH": {
        "name": "Results Path",
        "description": "The path in a GCP bucket where you would like to send the results of the protocol. \
            Leave blank if you don't want to send the results to a GCP bucket. \
                This could be in the same bucket as your data, or a different one.",
        "value": "",
    },
    "CREATE_VM": {
        "name": "Create VM",
        "description": "Whether or not to automatically create a VM instance on protocol start.",
        "value": "No",
    },
    "DELETE_VM": {
        "name": "Delete VM",
        "description": "Whether or not to immediately and automatically delete the VM instance on protocol completion.",
        "value": "No",
    },
    "index": [
        "PUBLIC_KEY",
        "GCP_PROJECT",
        "DATA_PATH",
        "GENO_BINARY_FILE_PREFIX",
        "NUM_INDS",
        "NUM_THREADS",
        "NUM_CPUS",
        "ZONE",
        "BOOT_DISK_SIZE",
        "DATA_HASH",
        "IP_ADDRESS",
        "PORTS",
        "AUTH_KEY",
        "SEND_RESULTS",
        "RESULTS_PATH",
        "CREATE_VM",
        "DELETE_VM",
    ],
}


def default_user_parameters(study_type: str, demo: bool = False) -> dict:
    parameters: dict = deepcopy(DEFAULT_USER_PARAMETERS)
    if demo:
        parameters["GCP_PROJECT"]["value"] = SERVER_GCP_PROJECT
        if study_type == "MPC-GWAS":
            parameters["NUM_INDS"]["value"] = "1000"
        elif study_type == "PCA":
            parameters["NUM_INDS"]["value"] = "2504"
        elif study_type == "SF-GWAS":
            parameters["NUM_INDS"]["value"] = "2000"
    return parameters


def broad_user_parameters() -> dict:
    parameters: dict = deepcopy(DEFAULT_USER_PARAMETERS)
    parameters["GCP_PROJECT"]["value"] = SERVER_GCP_PROJECT
    parameters["NUM_INDS"]["value"] = "0"
    return parameters


BROAD_VM_SOURCE_IP_RANGES = [
    "69.173.112.0/21",
    "69.173.127.232/29",
    "69.173.127.128/26",
    "69.173.127.0/25",
    "69.173.127.240/28",
    "69.173.127.224/30",
    "69.173.127.230/31",
    "69.173.120.0/22",
    "69.173.127.228/32",
    "69.173.126.0/24",
    "69.173.96.0/20",
    "69.173.64.0/19",
    "69.173.127.192/27",
    "69.173.124.0/23",
]

SOURCE_IP_RANGES = BROAD_VM_SOURCE_IP_RANGES + [
    "35.235.240.0/20",  # IAP TCP forwarding
    "10.128.0.0/9",  # Google internal IPs
    "10.0.0.10",  # for auto-configured vms
    "10.0.1.10",
    "10.0.2.10",
    "10.0.3.10",
    "10.0.4.10",
    "10.0.5.10",
    "10.0.6.10",
    "10.0.7.10",
    "10.0.8.10",
    "10.0.9.10",
    "10.0.10.10",
]

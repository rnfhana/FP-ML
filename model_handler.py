# =============================================================================
# FILE: model_handler.py
# DESKRIPSI: Modul untuk menangani pemuatan model FastAI dan prediksi.
#            Versi ini sudah berisi patch untuk kompatibilitas Windows.
# =============================================================================

import os
import platform
import pathlib
import random
import warnings
from PIL import Image

# Mengabaikan beberapa peringatan dari library internal
warnings.filterwarnings("ignore", category=UserWarning, module="torch.utils.data")
warnings.filterwarnings("ignore", category=FutureWarning)

# --- Cek dan Import Library FastAI ---
try:
    from fastai.vision.all import load_learner, PILImage
    FASTAI_AVAILABLE = True
except ImportError:
    FASTAI_AVAILABLE = False
    print("="*50)
    print("PERINGATAN: Library FastAI tidak ditemukan.")
    print("Silakan install dengan perintah: pip install fastai")
    print("="*50)

# --- Kelas Utama untuk Mengelola Model ---
class ModelHandler:
    """
    Kelas untuk menangani semua operasi terkait model:
    memuat model, melakukan pra-pemrosesan gambar, dan prediksi.
    """
    
    def __init__(self, model_path="my_model.pkl"):
        """Inisialisasi handler, mengatur path model dan memuatnya."""
        self.model_path = model_path
        self.model = None
        self.waste_types = [] # Akan diisi dari vocabulary model
        
        if FASTAI_AVAILABLE:
            self.load_model()
        else:
            # Set default classes jika fastai tidak ada
            self.waste_types = ['cardboard', 'glass', 'metal', 'paper', 'plastic']
            print("FastAI tidak tersedia. Prediksi akan menggunakan data dummy.")
    
    def load_model(self):
        """
        Memuat model FastAI. Secara otomatis menangani masalah path antara Windows dan Linux/macOS.
        """
        try:
            if not os.path.exists(self.model_path):
                raise FileNotFoundError(f"File model tidak ditemukan di: {self.model_path}")

            # SOLUSI: Terapkan 'patch' jika berjalan di Windows untuk memuat model dari Linux/macOS
            if platform.system() == "Windows":
                temp = pathlib.PosixPath
                try:
                    pathlib.PosixPath = pathlib.WindowsPath
                    self.model = load_learner(self.model_path)
                finally:
                    # Selalu kembalikan ke kondisi semula setelah selesai
                    pathlib.PosixPath = temp
            else:
                # Untuk Linux, macOS, atau sistem lain, muat secara normal
                self.model = load_learner(self.model_path)
            
            # Perbarui tipe kelas sampah (waste_types) dari vocabulary model
            if hasattr(self.model, 'dls') and hasattr(self.model.dls, 'vocab'):
                self.waste_types = list(self.model.dls.vocab)
            else:
                # Fallback jika vocab tidak ditemukan
                self.waste_types = ['Cardboard', 'Glass', 'Metal', 'Paper', 'Plastic']
                
        except Exception as e:
            print(f"❌ Gagal memuat model: {str(e)}")
            self.model = None
            # Re-raise the exception to be caught by Streamlit
            raise e
    
    def predict(self, image: Image.Image):
        """
        Melakukan prediksi pada sebuah gambar (objek PIL.Image).
        """
        if not self.is_model_loaded():
            print("   > Peringatan: Model tidak siap, menggunakan prediksi dummy.")
            return self._dummy_prediction()
        
        try:
            pred, pred_idx, probs = self.model.predict(image)
            prediction = str(pred).capitalize()
            probabilities = {name.capitalize(): float(p) for name, p in zip(self.waste_types, probs)}
            return prediction, probabilities
            
        except Exception as e:
            print(f"   > Terjadi error saat prediksi: {str(e)}")
            return self._dummy_prediction()

    def is_model_loaded(self):
        """Mengecek apakah model sudah berhasil dimuat."""
        return self.model is not None and FASTAI_AVAILABLE
        
    def _dummy_prediction(self):
        """Menghasilkan prediksi acak jika model tidak tersedia."""
        if not self.waste_types:
             self.waste_types = ['Cardboard', 'Glass', 'Metal', 'Paper', 'Plastic']
        prediction = random.choice(self.waste_types).capitalize()
        probs = [random.random() for _ in self.waste_types]
        total = sum(probs)
        probs = [p / total for p in probs]
        probabilities = {name.capitalize(): p for name, p in zip(self.waste_types, probs)}
        return prediction, probabilities
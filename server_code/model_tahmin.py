from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)

        # Dropdown'lar için seçenekler
        self.tur_dropdown.items = [
            ("Kedi", 0),
            ("Köpek", 1)
        ]
        
        self.sistem_dropdown.items = [
            ("Bilinmiyor", 0),
            ("Boşaltım", 1),
            ("Deri", 2),
            ("Dolaşım", 3),
            ("Mix", 4),
            ("Sindirim", 5),
            ("Sinir", 6),
            ("Solunum", 7)
        ]

        self.abdominal_agri_dropdown.items = [
            ("Yok", 0),
            ("Var", 1)
        ]

        self.genel_durum_dropdown.items = [
            ("Yok", 0),
            ("Var", 1)
        ]

        self.idar_problemi_dropdown.items = [
            ("Yok", 0),
            ("Var", 1)
        ]

        self.inkordinasyon_dropdown.items = [
            ("Yok", 0),
            ("Var", 1)
        ]

        self.ishal_dropdown.items = [
            ("Yok", 0),
            ("Var", 1)
        ]

        self.istahsizlik_dropdown.items = [
            ("Yok", 0),
            ("Var", 1)
        ]

        self.kanama_dropdown.items = [
            ("Yok", 0),
            ("Var", 1)
        ]

        # Kusma dropdown için seçenekler
        self.kusma_dropdown.items = [
            ("Yok", 0),
            ("Var", 1)
        ]

        # Oksuruk dropdown için seçenekler
        self.oksuruk_dropdown.items = [
            ("Yok", 0),
            ("Var", 1)
        ]

    def tahmin_et_button_click(self, **event_args):
        """Bu metod butona tıklandığında çağrılır"""
        
        # tur dropdown değerini al
        tur = self.tur_dropdown.selected_value

        # sistem dropdown değerini al
        sistem = self.sistem_dropdown.selected_value
        
        # float değerlerini al
        cBasebC = float(self.cBasebC_textbox.text)
        cBaseEcfc = float(self.cBaseEcfc_textbox.text)
        HCO3Pc = float(self.HCO3Pc_textbox.text)
        p50c = float(self.p50c_textbox.text)
        cHCO3Pst = float(self.cHCO3Pst_textbox.text)
        cNa = float(self.cNa_textbox.text)
        FHHb = float(self.FHHb_textbox.text)
        sO2 = float(self.sO2_textbox.text)
        GRAN = float(self.GRAN_textbox.text)
        LYM = float(self.LYM_textbox.text)
        MON_A = float(self.MON_A_textbox.text)
        HCT = float(self.HCT_textbox.text)
        MCH = float(self.MCH_textbox.text)
        MCHC = float(self.MCHC_textbox.text)
        
        # abdominal_agri dropdown değerini al
        abdominal_agri = self.abdominal_agri_dropdown.selected_value
        
        # genel_durum dropdown değerini al
        genel_durum = self.genel_durum_dropdown.selected_value
        
        # idar_problemi dropdown değerini al
        idar_problemi = self.idar_problemi_dropdown.selected_value
        
        # inkordinasyon dropdown değerini al
        inkordinasyon = self.inkordinasyon_dropdown.selected_value

        # ishal dropdown değerini al
        ishal = self.ishal_dropdown.selected_value
        
        # istahsizlik dropdown değerini al
        istahsizlik = self.istahsizlik_dropdown.selected_value

        # kanama dropdown değerini al
        kanama = self.kanama_dropdown.selected_value
        
        # kusma dropdown değerini al
        kusma = self.kusma_dropdown.selected_value
        
        # oksuruk dropdown değerini al
        oksuruk = self.oksuruk_dropdown.selected_value
        
        # Model tahmini yapma
        sonuc = anvil.server.call(
            'model_tahmin', 
            [tur, sistem, cBasebC, cBaseEcfc, HCO3Pc, p50c, cHCO3Pst, cNa, FHHb, sO2, GRAN, LYM, MON_A, HCT, MCH, MCHC, abdominal_agri, genel_durum, idar_problemi, inkordinasyon, ishal, istahsizlik, kanama, kusma, oksuruk]
        )

        # Sonucu göster
        self.sonuc_label.text = f"Tahmin Sonucu: {sonuc}"
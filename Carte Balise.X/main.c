/******************************************************************************/
/**************** Carte Balise : DSPIC33FJ128MC804 ****************************/
/******************************************************************************/
/* Fichier 	: main.c
 * Auteur  	: Quentin
 * Revision	: 1.0
 * Date		: 04 novembre 2015, 23:08
 *******************************************************************************
 *
 *
 ******************************************************************************/

#include "system.h"



/******************************************************************************/
/************************ Configurations Bits *********************************/
/******************************************************************************/

// DSPIC33FJ128MC804 Configuration Bit Settings

// FBS
#pragma config BWRP = WRPROTECT_OFF     // Boot Segment Write Protect (Boot Segment may be written)
#pragma config BSS = NO_FLASH           // Boot Segment Program Flash Code Protection (No Boot program Flash segment)
#pragma config RBS = NO_RAM             // Boot Segment RAM Protection (No Boot RAM)

// FSS
#pragma config SWRP = WRPROTECT_OFF     // Secure Segment Program Write Protect (Secure segment may be written)
#pragma config SSS = NO_FLASH           // Secure Segment Program Flash Code Protection (No Secure Segment)
#pragma config RSS = NO_RAM             // Secure Segment Data RAM Protection (No Secure RAM)

// FGS
#pragma config GWRP = OFF               // General Code Segment Write Protect (User program memory is not write-protected)
#pragma config GSS = OFF                // General Segment Code Protection (User program memory is not code-protected)

// FOSCSEL
#pragma config FNOSC = FRC              // Oscillator Mode (Internal Fast RC (FRC) w/ PLL)
#pragma config IESO = OFF //ON          // Internal External Switch Over Mode (Start-up device with FRC, then automatically switch to user-selected oscillator source when ready)

// FOSC
#pragma config POSCMD = NONE            // Primary Oscillator Source (Primary Oscillator Disabled)
#pragma config OSCIOFNC = OFF            // OSC2 Pin Function (OSC2 pin has digital I/O function)
#pragma config IOL1WAY = OFF            // Peripheral Pin Select Configuration (Allow Multiple Re-configurations)
#pragma config FCKSM = CSECMD  //CSDCMD           // Clock Switching and Monitor (Both Clock Switching and Fail-Safe Clock Monitor are disabled)

// FWDT
#pragma config WDTPOST = PS32768        // Watchdog Timer Postscaler (1:32,768)
#pragma config WDTPRE = PR128           // WDT Prescaler (1:128)
#pragma config WINDIS = OFF             // Watchdog Timer Window (Watchdog Timer in Non-Window mode)
#pragma config FWDTEN = OFF             // Watchdog Timer Enable (Watchdog timer enabled/disabled by user software)

// FPOR
#pragma config FPWRT = PWR128           // POR Timer Value (128ms)
#pragma config ALTI2C = ON              // Alternate I2C  pins (I2C mapped to ASDA1/ASCL1 pins)
#pragma config LPOL = ON                // Motor Control PWM Low Side Polarity bit (PWM module low side output pins have active-high output polarity)
#pragma config HPOL = ON                // Motor Control PWM High Side Polarity bit (PWM module high side output pins have active-high output polarity)
#pragma config PWMPIN = ON              // Motor Control PWM Module Pin Mode bit (PWM module pins controlled by PORT register at device Reset)

// FICD
#pragma config ICS = PGD2               // Comm Channel Select (Communicate on PGC2/EMUC2 and PGD2/EMUD2)
#pragma config JTAGEN = OFF             // JTAG Port Enable (JTAG is Disabled)



/******************************************************************************/
/********************* DECLARATION DES VARIABLES GLOBALES *********************/
/******************************************************************************/


/******************************************************************************/
/******************************************************************************/
/******************************************************************************/

int main(int argc, char** argv)
{
    
    /**************************************************************************/
    /*************************** INIT ROBOT ***********************************/
    /**************************************************************************/

    init_system();
    delay_ms(1000);
    
    
    //envoit_pwm(100); //30
    while(1)
    {
        if (BOUTON1 == 0)
        {
            LED1 = 0;
            P2DC1 = 2350;
            //envoit_pwm(0);
        }
        else
        {
            LED1 = 1;
            P2DC1 = 1600;
        }
        
        //PDC1=36850;
        
        if (BOUTON2 == 0 && BOUTON3 == 0)
            // MODE OFF
            envoit_pwm(0, LED);
        else if (BOUTON2 == 1 && BOUTON3 == 1)
            // MODE ON
            //envoit_pwm(100, LED);
        {
            static double valeur = 10;
            static int8_t sens = 1;
            
            if (sens == 0)
            {
                valeur+=0.006;
                if (valeur >= 100)
                {
                    sens = 1;
                    valeur = 10;    
                        
                }
            }
            else if (sens == 1)
            {
                valeur+=0.01;
                envoit_pwm(valeur, LED);
                if (valeur >= 100)
                    sens = 2;
            }
            else if (sens == 2)
            {
                valeur -=0.01;
                envoit_pwm(valeur, LED);
                if (valeur <= 30)
                    sens = 3;
            }
            else if (sens == 3)
            {
                valeur +=0.01;
                envoit_pwm(valeur, LED);
                if (valeur >= 100)
                    sens = 4;
            }       
            else 
            {
                valeur -= 0.008;
                envoit_pwm(valeur, LED);
                if (valeur <= 10)
                    sens = 0;
            }
        }
        else if (BOUTON2 == 0 && BOUTON3 == 1)
        {
            // BLINK_SLOW
            static double valeur = 5;
            static int8_t sens = 1;
            if (sens == 1 && valeur < 100)
            {
                valeur +=0.005;
                envoit_pwm(valeur, LED);
                if (valeur >= 100)
                    sens = -1;
            }
            else
            {
                valeur -=0.005;
                envoit_pwm(valeur, LED);
                if (valeur <= 5)
                    sens = 1;
            }
                   
            
        }
        else if (BOUTON2 == 1 && BOUTON3 == 0)
        {
            //BLINK_FAST
            static double valeur = 5;
            static int8_t sens = 1;
            if (sens == 1 && valeur < 100)
            {
                valeur +=0.05;
                envoit_pwm(valeur, LED);
                if (valeur >= 100)
                    sens = -1;
            }
            else
            {
                valeur -=0.05;
                envoit_pwm(valeur, LED);
                if (valeur <= 5)
                    sens = 1;
            }
        }
    }
    
    while(1);
    return (EXIT_SUCCESS);
}

